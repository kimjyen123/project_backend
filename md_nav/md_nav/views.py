from django.shortcuts import render
from meetings.models import Doctor, Meeting, Customer, Device, Recording

def home(request):
    doctors = Doctor.objects.all()
    meetings = Meeting.objects.all()
    customers = Customer.objects.all()
    devices = Device.objects.all()
    recordings = Recording.objects.all()

    return render(request, 'index.html', {
        'doctors': doctors,
        'meetings': meetings,
        'customers': customers,
        'devices': devices,
        'recordings': recordings
    })
