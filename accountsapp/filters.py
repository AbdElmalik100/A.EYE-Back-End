from django_filters.filterset import FilterSet
from .models import *


class CustomUserFilter(FilterSet):
    class Meta:
        model = CustomUser
        fields = ['username']