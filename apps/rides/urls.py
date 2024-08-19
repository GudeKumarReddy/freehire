from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.rides.views import LocationViewSet, NeedRideViewSet

router = DefaultRouter()
router.register('user-location', LocationViewSet)
router.register('ride-request', NeedRideViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
