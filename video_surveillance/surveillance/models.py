from django.db import models

class LastFrame(models.Model):
    frame = models.FileField(upload_to='frames/')  # لتخزين الفريم كملف
    timestamp = models.DateTimeField()  # لتخزين التوقيت
