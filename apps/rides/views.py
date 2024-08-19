from rest_framework import viewsets

from apps.rides.models import Location, NeedRide
from apps.rides.seralizers import LocationSerializer, NeedRideSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class NeedRideViewSet(viewsets.ModelViewSet):
    queryset = NeedRide.objects.all()
    serializer_class = NeedRideSerializer