from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *





class CustomUserSerializer(UserSerializer):
    # patient_profile = PatientProfileSerializer()
    # doctor_profile = DoctorProfileSerializer()
    class Meta:
        model = get_user_model()
        exclude = ['groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'password']
    
class PatientProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only = True)
    class Meta:
        model = PatientProfile
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only = True)
    class Meta:
        model = DoctorProfile
        fields = '__all__'


