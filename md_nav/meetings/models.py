from django.db import models
from django.utils import timezone

def default_posted_timestamp():
    return timezone.datetime(2024, 1, 1)

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100, default='null')
    last_name = models.CharField(max_length=100, default='null')
    hospital = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    posted_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Meeting(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    meeting_date = models.DateTimeField()
    instrument_name = models.CharField(max_length=255)
    instrument_specifications = models.CharField(max_length=255, default='null')
    meeting_note = models.TextField()
    customer_questions = models.TextField()
    posted_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.first_name} {self.doctor.last_name} - {self.meeting_date}"
    
# Secondary Database Models
class Customer(models.Model):
    name = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='photos/')
    publications = models.TextField()
    collaborators = models.TextField()
    linkedin_info = models.URLField()
    google_news = models.TextField()
    posted_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    device_name = models.CharField(max_length=255, default='null')
    device_description = models.CharField(max_length=255, default='null')
    device_catalog = models.CharField(max_length=255, default='null')
    summary_of_recent_papers = models.TextField()
    manuals = models.TextField()
    posted_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_name

class Recording(models.Model):
    recording_data = models.TextField()
    posted_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording for {self.doctor.first_name} {self.doctor.last_name}"
