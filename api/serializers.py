from rest_framework import serializers
from .models import *


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class DoctorDetectionResultsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetectionResults
        fields = '__all__'

class PatientDetectionResultsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetectionResults
        fields = '__all__'
