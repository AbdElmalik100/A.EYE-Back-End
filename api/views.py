from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import joblib
import pickle
import torch
# Create your views here.

model = joblib.load('Diabetic Detection.pkl')
print("Model Initialized!")


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer


class DoctorDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetectionResults.objects.all()
    serializer_class = DoctorDetectionResultsSerialzer

class PatientDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = PatientDetectionResults.objects.all()
    serializer_class = PatientDetectionResultsSerialzer

    def perform_create(self, serializer):
        result = serializer.save()
        image_url = serializer.data['image']
        print(image_url)


        # model = joblib.load('blindness_detection_model.pkl')
        # model = torch.load('checkpoint.pth', map_location=torch.device('cpu'))
        print(dir(model))

        # detectionInstance.test(image_url)
    