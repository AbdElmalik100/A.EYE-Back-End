from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("patient", PatientProfileViewSet)
router.register("doctor", DoctorProfileViewSet)
router.register('users', CustomUserViewSet)

urlpatterns = [
    path("accounts/", include(router.urls))
]
