import random

from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import OTP
from django.contrib.auth import get_user_model
User = get_user_model()


def create_otp_service(email):
    otp = random.randint(10000, 99999)
    otp_row, created = OTP.objects.get_or_create(email=email)
    otp_row.otp, otp_row.created_at = otp, timezone.now()
    otp_row.save()
    return otp


def verify_otp_service(data):
    otp = OTP.objects.filter(email=data['email'], otp=data['otp'])
    if otp.exists() and not otp.last().is_expired():
        otp.delete()
        try:
            return User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise ValidationError({"detail": "User does not exist."})
    return False


def get_tokens_for_user(user):
    print(user)
    refresh = RefreshToken.for_user(user)

    user_detail = {
        "name": user.full_name,
        "email": user.email,
        "gender": user.gender,
        "type": user.type,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
        "tokens": {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },
    }

    return user_detail