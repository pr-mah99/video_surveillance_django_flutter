import os
import cv2
from django.conf import settings
import time
import wave
import requests
import pyaudio
import threading
from queue import Queue
from moviepy.editor import VideoFileClip, AudioFileClip
from concurrent.futures import ThreadPoolExecutor
from utils import (compress_frame_jpeg, encrypt_frame_data, save_frame,
                   save_encrypted_data, save_video)

# إعدادات الصوت
audio_format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024
audio_folder = 'media/audio'
os.makedirs(audio_folder, exist_ok=True)

frame_counter = 0
counter_lock = threading.Lock()
recording_audio = True
running = True  # متغير للتحكم في حالة التشغيل

# تعريف الـ Queue للإطارات
frame_queue = Queue()

# === الوظائف الرئيسية === #

def process_frame(frame, sensor_id, encryption_key):
    timestamp = int(time.time())

    # ضغط الصورة باستخدام DCT وتحويلها إلى بايتات
    compressed_dct_bytes = compress_frame_jpeg(frame)
    if compressed_dct_bytes is None:
        return None, None

    # حفظ الصورة المضغوطة في ملف
    compressed_file_path = save_frame(compressed_dct_bytes, f'sensor_frame_{sensor_id}_{timestamp}_compressed.jpg')
    
    # تشفير البيانات المضغوطة
    nonce, ciphertext, tag = encrypt_frame_data(compressed_dct_bytes, encryption_key)
    encrypted_file_path = save_encrypted_data(ciphertext, f'sensor_frame_{sensor_id}_{timestamp}_encrypted.jpg')

    # احسب حجم الصورة الأصلية والمضغوطة
    original_encoded = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])[1].tobytes()
    original_size = len(original_encoded)
    compressed_size = len(compressed_dct_bytes)

    if compressed_size > original_size:
        print(f"Original frame size: {original_size:,} bytes")
        print(f"Compressed frame size: {compressed_size:,} bytes")
        print("-" * 15)  # خط فاصل
        print(f"Warning: Compressed size is larger than original!")
        return compressed_file_path, encrypted_file_path, nonce, ciphertext, tag

    reduction_percentage = ((original_size - compressed_size) / original_size) * 100
    global frame_counter
    with counter_lock:
        frame_counter += 1
        example_number = frame_counter

    print(f"Original frame size: {original_size:,} bytes")
    print(f"Compressed frame size: {compressed_size:,} bytes")
    print("-" * 15)  # خط فاصل
    print(f"Frame {example_number}: Size reduction: ~{reduction_percentage:.1f}%")

    # إضافة البيانات المضغوطة إلى الـ Queue
    frame_queue.put((compressed_dct_bytes, timestamp))

    return compressed_file_path, encrypted_file_path, nonce, ciphertext, tag


def send_frame_to_api():
    global running
    while running:
        # سحب الفريمات من الـ Queue وإرسالها
        if not frame_queue.empty():
            compressed_dct_bytes, timestamp = frame_queue.get()
            
            url = settings.API_URL
            files = {'frame': ('frame.jpg', compressed_dct_bytes, 'image/jpeg')}
            data = {'timestamp': timestamp}

            try:
                response = requests.post(url, files=files, data=data)
                print(response.json())  # طباعة الرد من الخادم
            except Exception as e:
                print(f"Error sending frame to API: {e}")
            
            frame_queue.task_done()


def record_audio(file_name):
    global running
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    frames = []
    print(f"Recording audio to {file_name}...")
    while running:
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(audio_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Audio recorded and saved to {file_name}.")


def merge_audio_video(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Video with audio saved to: {output_path}")
    except Exception as e:
        print(f"Error merging audio and video: {e}")


def main():
    global running
    cap = cv2.VideoCapture(0)
    encryption_key = b'1234567890abcdef'
    frames_before = []

    if not cap.isOpened():
        print("Failed to open video source")
        return

    sensor_id = 'sensor_01'
    timestamp = int(time.time())
    audio_file_before = os.path.join(audio_folder, f'audio_before_{sensor_id}_{timestamp}.wav')
    recording_audio = True
    audio_thread_before = threading.Thread(target=record_audio, args=(audio_file_before,))
    audio_thread_before.start()

    # إنشاء ThreadPoolExecutor لإرسال الفريمات
    with ThreadPoolExecutor(max_workers=4) as executor:
        # بدء إرسال الفريمات باستخدام الخيوط
        executor.submit(send_frame_to_api)

        while running:
            ret, frame = cap.read()
            if ret:
                frames_before.append(frame)
                process_frame(frame, sensor_id, encryption_key)  # إضافة الفريمات إلى الـ Queue
                cv2.imshow('Original Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Key 'q' pressed, stopping...")
                    running = False  # إيقاف جميع العمليات عند الضغط على 'q'
                    break
            else:
                print("Failed to capture frame")

        # إيقاف تسجيل الصوت
        recording_audio = False
        audio_thread_before.join()

        # تكوين الفيديو بعد إيقاف التسجيل
        if frames_before:
            frame_height, frame_width = frames_before[0].shape[:2]
            video_output_path_before = f'media/videos/sensor_video_before_{sensor_id}_{timestamp}.avi'
            save_video(frames_before, video_output_path_before, fps=30, frame_size=(frame_width, frame_height))
            video_output_path_after = f'media/videos/sensor_video_after_{sensor_id}_{timestamp}.mp4'
            save_video(frames_before, video_output_path_after, fps=30, frame_size=(frame_width, frame_height), encryption_key=encryption_key)
            merge_audio_video(video_output_path_before, audio_file_before, video_output_path_after)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
