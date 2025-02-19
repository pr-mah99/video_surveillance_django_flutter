# urls.py (الرئيسي)
from django.urls import path, include  # إضافة استيراد path و include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from surveillance.views import FrameView  # استيراد FrameView من views.py


# إنشاء Router
router = DefaultRouter()

# روابط الـ URLs
urlpatterns = [
    path('', include(router.urls)),  # تضمين الروابط الخاصة بالـ ViewSet في الرابط الجذري
    path('frames/', FrameView.as_view(), name='update-frame'),  # تسجيل API لـ FrameView
    path('api/', include('surveillance.urls')),  # إذا كنت تستخدم تطبيق معين مثل yourapp
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # إعداد الوصول للملفات في وضع التطوير
