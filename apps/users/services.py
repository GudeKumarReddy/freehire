import random

from django.utils import timezone

from apps.users.models import OTP


def create_otp_service(email):
    otp = random.randint(10000, 99999)
    otp_row, created = OTP.objects.get_or_create(email=email)
    otp_row.otp, otp_row.created_at = otp, timezone.now()
    otp_row.save()
    return otp
