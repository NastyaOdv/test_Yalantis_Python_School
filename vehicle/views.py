import django_filters
from django.db import IntegrityError
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleSerializerSetDriver, VehicleSerializerSetDriverCreate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from django_filters import FilterSet
from driver.models import Driver
CHOICES=[('yes','yes'),('no','no')]
class VehicleFilter(FilterSet):
    def filter_driver(self, queryset, name, value):
        if value=='yes':
            queryset=queryset.filter(driver_id__isnull=False)
        else:
            queryset = queryset.filter(driver_id__isnull=True)
        return queryset
    with_drivers=django_filters.ChoiceFilter(label='Choose option:', method='filter_driver', choices=CHOICES)
class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_class = VehicleFilter

class VehicleSetDriver(viewsets.GenericViewSet):
    queryset = Vehicle.objects.all()
    basename = 'set_driver'
    serializer_class = VehicleSerializerSetDriver
    serializer_action_classes = {
        'set_driver':VehicleSerializerSetDriverCreate
    }
    @action(detail=True,methods=['post'],name='Set Driver.')
    def set_driver(self,request,pk=None):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        driver_id = validated_data.get('driver_id')
        vehicle = self.queryset.get(pk=pk)
        if not driver_id:
            vehicle.driver_id=None
        elif vehicle.driver_id is not None:
            raise ValueError("")
        else:
            vehicle.driver_id = Driver.objects.get(pk=driver_id)
        try:
            vehicle.save()
        except IntegrityError:
            raise ValueError(" ")
        return Response(self.serializer_class(vehicle).data)
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(VehicleViewSet,self).get_serializer_class()





