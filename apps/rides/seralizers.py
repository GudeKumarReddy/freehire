from rest_framework import serializers
from .models import Location, NeedRide


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class NeedRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedRide
        fields = '__all__'