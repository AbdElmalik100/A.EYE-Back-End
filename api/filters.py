from django_filters import rest_framework as filters
from django.db.models import OuterRef, Subquery
from .models import *



class PatientsFilter(filters.FilterSet):
    detection_type = filters.CharFilter(field_name='detection_type', label='Detection Type', method='filter_by_detection')

    class Meta:
        model = Patients
        fields = ['doctor', 'detection_type']

    def filter_by_detection(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(
                doctor_patients_detections__id__in=Subquery(
                    DoctorDetectionResults.objects.filter(
                        patient_id=OuterRef('id')
                    ).order_by('-created_at').values('id')[:1]
                ),
                doctor_patients_detections__result_class=value
            ).distinct()
        return queryset



class DoctorDetectionResultsFilter(filters.FilterSet):
    class Meta:
        model = DoctorDetectionResults
        fields = ['result', 'patient']


class PatientDetectionResultsFilter(filters.FilterSet):
    class Meta:
        model = PatientDetectionResults
        fields = ['result', 'patient']