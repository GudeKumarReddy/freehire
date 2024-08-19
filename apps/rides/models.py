from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import BaseModel
User = get_user_model()


class Location(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    land_mark = models.CharField(max_length=199)


VEHICLE_TYPE = (
    ('2_wheeler', '2 Wheeler'),
    ('4_wheeler', '4 Wheeler')
)

RIDE_STATUS = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('completed', 'Completed')
)


class NeedRide(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(Location, related_name='pickup_location', on_delete=models.CASCADE)
    drop_location = models.ForeignKey(Location, related_name='drop_location', on_delete=models.CASCADE)
    current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE)
    ride_status = models.CharField(max_length=20, choices=RIDE_STATUS, default='pending')


# class GiveRide(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     pickup_location = models.ForeignKey(Location, related_name='pickup_location', on_delete=models.CASCADE)
#     drop_location = models.ForeignKey(Location, related_name='drop_location', on_delete=models.CASCADE)
#     current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE)


