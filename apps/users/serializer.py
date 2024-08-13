from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import OTP

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    is_18_plus = serializers.BooleanField(write_only=True, required=True)
    mobile_number = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate_is_18_plus(self, value):
        if not value:
            raise serializers.ValidationError("You should be 18 plus to sign up to this application!")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User already exists with the given email!")
        return value

    def validate(self, data):
        if User.objects.filter(email=data['email'], mobile_number=data['mobile_number']).exists():
            raise serializers.ValidationError("A user with this email and mobile number already exists.")
        return data

    def create(self, validated_data):
        validated_data.pop('is_18_plus', None)
        user = User.objects.create_user(**validated_data)
        return user


class OtpSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(read_only=True)
    class Meta:
        fields = "__all__"
        model = OTP
