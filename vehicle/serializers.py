from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Vehicle
from driver.models import Driver
class VehicleSerializer(serializers.ModelSerializer):
    def validate_plate_number(self,plate_number):
        if (len(plate_number)==10 and plate_number[0].isalpha() and plate_number[1].isalpha() and plate_number[8].isalpha()
                and plate_number[9].isalpha() and plate_number[2]==' 'and plate_number[7]==' '):
                return plate_number.upper()
        raise serializers.ValidationError("Incorrect plate_number")


    class Meta:
        model = Vehicle
        fields = ('id','make','model','created_at','update_at', 'driver_id','plate_number')
class VehicleSerializerSetDriver(serializers.ModelSerializer):
    def validate_driver_id(self,driver_id):
        if driver_id:
            try:
                Driver.objects.get(pk=driver_id)
            except ObjectDoesNotExist:
                raise serializers.ValidationError('')
        return driver_id


    class Meta:
        model = Vehicle
        fields = '__all__'
        read_only_fields = ('id','make','model','created_at','update_at', 'driver_id','plate_number')
class VehicleSerializerSetDriverCreate(VehicleSerializerSetDriver):
    driver_id = serializers.IntegerField(required=True,allow_null=True)
