import base64
import os
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

# إنشاء مجلد لحفظ الفريمات إذا لم يكن موجودًا
os.makedirs('media/frames', exist_ok=True)

class FrameView(APIView):
    # تحديد المجلد الذي سيتم تخزين الفريمات فيه
    frames_directory = 'media/frames'

    # استخدام MultiPartParser و FormParser للتعامل مع البيانات المرسلة
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        # إذا كانت هناك فريمات محفوظة في الذاكرة
        frame_files = os.listdir(self.frames_directory)
        if frame_files:
            # الحصول على آخر فريم تم تخزينه (الفريم الأخير في المجلد)
            last_frame_file = frame_files[-1]
            frame_path = os.path.join(self.frames_directory, last_frame_file)

            # قراءة الفريم من الملف وتحويله إلى base64
            with open(frame_path, 'rb') as f:
                frame_data = f.read()
                frame_base64 = base64.b64encode(frame_data).decode('utf-8')  # تحويل البيانات إلى Base64

            # إرجاع الفريم مع التوقيت الحالي بصيغة ISO
            return Response({
                "frame": frame_base64,
                "timestamp": datetime.now().isoformat()  # التوقيت بصيغة ISO
            }, status=status.HTTP_200_OK)

        return Response({"message": "No frames available"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        # استلام الفريم من البيانات المرسلة عبر POST
        frame_file = request.FILES.get('frame')
        timestamp = request.data.get('timestamp')

        if frame_file:
            # إنشاء اسم للفريم بناءً على التوقيت (timestamp) لتخزينه بشكل فريد
            frame_filename = f"frame_{timestamp}.jpg"
            frame_path = os.path.join(self.frames_directory, frame_filename)

            # تخزين الفريم في المجلد
            with open(frame_path, 'wb') as f:
                for chunk in frame_file.chunks():
                    f.write(chunk)

            # إرجاع رسالة نجاح
            return Response({"message": "Frame received successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "No frame found"}, status=status.HTTP_400_BAD_REQUEST)
