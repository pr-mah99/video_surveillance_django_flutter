# serializers.py
from rest_framework import serializers
from .models import LastFrame

class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastFrame
        fields = ['frame', 'timestamp']
