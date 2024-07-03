from django.db import models
from accountsapp.models import *
# Create your models here.


GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

class Patients(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 255, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length = 50, choices = GENDER, default = 'male')
    phone_number = models.CharField(max_length = 255)
    doctor = models.ForeignKey(DoctorProfile, on_delete = models.CASCADE, related_name = 'patients_doctor')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name.capitalize()} {self.last_name}"
        super(Patients, self).save(*args, **kwargs) # Call the real save() method

class DoctorDetectionResults(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='detected_image/doctors_patient', blank=True, null=True, default=None)
    result = models.CharField(max_length=255, blank=True, null=True)
    result_class = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    points = models.CharField(max_length=1000, blank=True, null=True)
    description_arabic = models.TextField(blank=True, null=True)
    points_arabic = models.CharField(max_length=1000, blank=True, null=True)
    patient = models.ForeignKey(Patients, on_delete = models.CASCADE, related_name = 'doctor_patients_detections', blank=True, null=True)


class PatientDetectionResults(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    image = models.ImageField(upload_to='detected_image/patients', blank=True, null=True, default=None)
    result_class = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    points = models.CharField(max_length=1000, blank=True, null=True)

    description_arabic = models.TextField(blank=True, null=True)
    points_arabic = models.CharField(max_length=1000, blank=True, null=True)
    patient = models.ForeignKey(PatientProfile, on_delete = models.CASCADE, related_name = 'patient_detections')

