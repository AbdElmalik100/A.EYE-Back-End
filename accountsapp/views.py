from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from djoser.views import UserViewSet
from .filters import CustomUserFilter


# Create your views here.


class CustomUserViewSet(UserViewSet):
    filterset_class = CustomUserFilter


class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    lookup_field = 'user'

class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    lookup_field = 'user'



