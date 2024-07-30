from rest_framework import serializers
from .models import Doctor, Meeting, Customer, Device, Recording


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'hospital', 'city', 'state']

class MeetingSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='doctor.first_name', read_only=True)
    last_name = serializers.CharField(source='doctor.last_name', read_only=True)
    doctor_hospital = serializers.CharField(source='doctor.hospital', read_only=True)

    class Meta:
        model = Meeting
        fields = ['id', 'first_name', 'last_name', 'doctor_hospital',
                  'meeting_date', 'instrument_name', 'instrument_specifications',
                  'meeting_note', 'customer_questions', 'posted_timestamp']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = '__all__'
