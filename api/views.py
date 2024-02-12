from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.



class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer


class DoctorDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetectionResults.objects.all()
    serializer_class = DoctorDetectionResultsSerialzer


class PatientDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = PatientDetectionResults.objects.all()
    serializer_class = PatientDetectionResultsSerialzer