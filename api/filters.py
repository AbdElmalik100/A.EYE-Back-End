from django_filters.filterset import FilterSet
from .models import *


class PatientDetectionResultsFilter(FilterSet):
    class Meta:
        model = PatientDetectionResults
        fields = ['result', 'patient']