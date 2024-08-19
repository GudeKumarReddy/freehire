from django.contrib import admin

from apps.rides.models import Location, NeedRide


class LocationAmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'land_mark']


class NeedRideAmin(admin.ModelAdmin):
    list_display = ['user', 'vehicle_type', 'ride_status']


admin.site.register(Location, LocationAmin)
admin.site.register(NeedRide, NeedRideAmin)
