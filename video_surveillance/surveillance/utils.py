import os
import cv2
from Crypto.Cipher import AES

def compress_frame_jpeg(frame, quality=50):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    result, encimg = cv2.imencode('.jpg', frame, encode_param)
    if not result:
        print("Failed to compress image using JPEG!")
        return None
    return encimg.tobytes()

def encrypt_frame_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext, tag

def decrypt_frame_data(ciphertext, nonce, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

def save_frame(encoded_image, filename, directory='media/frames'):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as f:
        f.write(encoded_image)
    print(f'Compressed image saved at: {file_path}')
    return file_path

def save_encrypted_data(data, filename, directory='media/encrypted'):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as f:
        f.write(data)
    print(f'Encrypted data saved at: {file_path}')
    return file_path

def save_video(frames, output_path, fps=30, frame_size=(640, 480), encryption_key=None):
    # تحديد الترميز المناسب لتنسيق MP4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') if output_path.endswith('.mp4') else cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    for frame in frames:
        out.write(frame)

    out.release()
    print(f'Video saved at: {output_path}')

    if encryption_key:
        # Encrypt the video file
        with open(output_path, 'rb') as video_file:
            video_data = video_file.read()
        nonce, ciphertext, tag = encrypt_frame_data(video_data, encryption_key)
        encrypted_video_path = save_encrypted_video(ciphertext, f'encrypted_{os.path.basename(output_path)}')
        return encrypted_video_path

    return output_path

def save_encrypted_video(data, filename, directory='media/encrypted_videos'):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as f:
        f.write(data)
    print(f'Encrypted video saved at: {file_path}')
    return file_path
