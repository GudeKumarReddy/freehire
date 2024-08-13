from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import sign_up, GenerateOTP

router = DefaultRouter()
router.register('send-otp', GenerateOTP)

urlpatterns = [
    path('signup/', sign_up),
    path('', include(router.urls)),

]
