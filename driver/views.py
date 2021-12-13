
from .serializers import DriverSerializer
from .models import Driver
import django_filters
from rest_framework.generics import get_object_or_404, GenericAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from django_filters import FilterSet

class DriverFilter(FilterSet):
    created_at__gte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte', input_formats=["%d-%m-%Y"])
    created_at__lte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte',
                                                    input_formats=["%d-%m-%Y"])
    class Meta:
        model = Driver
        fields = ['created_at__gte','created_at__lte']


class DriverListCreateView(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_class = DriverFilter


class SingleDriverView(RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer