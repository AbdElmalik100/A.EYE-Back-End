from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Contact)
admin.site.register(Patients)
admin.site.register(DoctorDetectionResults)
admin.site.register(PatientDetectionResults)