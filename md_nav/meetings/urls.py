from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, MeetingViewSet, CustomerViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
