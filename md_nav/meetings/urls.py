from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'meetings', views.MeetingViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'recordings', views.RecordingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
