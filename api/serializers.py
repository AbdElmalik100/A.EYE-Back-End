from rest_framework import serializers
from .models import *


class ContactSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class DoctorDetectionResultsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetectionResults
        fields = '__all__'

class PatientsSerializer(serializers.ModelSerializer):
    doctor_patients_detections = DoctorDetectionResultsSerialzer(many = True, read_only = True)

    class Meta:
        model = Patients
        fields = '__all__'
    

class PatientDetectionResultsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetectionResults
        fields = '__all__'
