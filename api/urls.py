from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register("contact", ContactViewSet)
router.register("patients", PatientsViewSet)
router.register("doctor-detection", DoctorDetectionResultsViewSet)
router.register("patient-detection", PatientDetectionResultsViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
