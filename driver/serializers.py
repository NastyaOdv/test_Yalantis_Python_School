from rest_framework import serializers

from .models import Driver
class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('id','first_name','last_name','created_at','update_at')
