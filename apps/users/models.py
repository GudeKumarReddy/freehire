from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.users.usermanager import CustomUserManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

USER_TYPE_CHOICES = (
    ('need_transportation', 'Need transportation'),
    ('give_transportation', 'Give Transportation')
)
class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    full_name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    mobile_number = models.CharField(max_length=13, unique=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

    profile_pic = models.ImageField(upload_to='uploads/', null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    is_18_plus = models.BooleanField(default=False)
    type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES, null=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class OTP(BaseModel):
    otp = models.CharField(max_length=5)
    email = models.CharField(max_length=255)

    def is_expired(self):
        # Check if the OTP is expired (5-minute expiration time)
        current_time = timezone.now()
        return (current_time - self.created_at).total_seconds() > 600  # 300 seconds = 5 minutes

