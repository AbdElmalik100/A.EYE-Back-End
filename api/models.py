from django.db import models
from accountsapp.models import *
# Create your models here.


GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Patients(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField()
    gender = models.CharField(max_length = 50, choices = GENDER, default = 'male')
    phone_number = models.CharField(max_length = 255)
    doctor = models.ForeignKey(DoctorProfile, on_delete = models.CASCADE, related_name = 'patients_doctor')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class DoctorDetectionResults(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    result = models.CharField(max_length=255)
    image = models.ImageField(upload_to='detected_image', blank=True, null=True, default=None)
    # image = models.CharField(max_length = 255, blank=True, null=True, default=None)
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE, related_name = 'doctor_patients_detections')

class PatientDetectionResults(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='detected_image', blank=True, null=True, default=None)
    # image = models.CharField(max_length = 255, blank=True, null=True, default=None)
    patient = models.ForeignKey(PatientProfile, on_delete = models.CASCADE, related_name = 'patient_detections')

