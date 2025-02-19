# urls.py
from django.urls import path
from .views import FrameView

urlpatterns = [
    path('frames/', FrameView.as_view(), name='frame_api'),
]
