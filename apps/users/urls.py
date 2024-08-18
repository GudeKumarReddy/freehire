from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import sign_up, GenerateOTP, UserLoginViewSet

router = DefaultRouter()
router.register('send-otp', GenerateOTP)
router.register('login', UserLoginViewSet)

urlpatterns = [
    path('signup/', sign_up),
    path('', include(router.urls)),

]
