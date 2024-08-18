import random

from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from apps.users.models import OTP
from apps.users.serializer import OtpSerializer, LoginSerializer
from apps.users.services import create_otp_service, verify_otp_service, get_tokens_for_user

User = get_user_model()


def return_response(data, success, message, status_code):
    return Response({
        'data': data,
        'success': success,
        'message': message,
        'status': status_code,
    }, status=status_code)


@api_view(['POST'])
def sign_up(request):
    is_18_plus = request.data.get('is_18_plus')
    if not is_18_plus:
        raise ValidationError({"message": "You should be 18 plus to sign up to this application!"})

    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        raise ValidationError({"message": "Users already exists with the given email!"})

    User.objects.create(**request.data)
    return return_response(data=None, success=True, message="Account created successfully!", status_code=201)


class GenerateOTP(viewsets.ModelViewSet):
    queryset = OTP.objects.all()
    serializer_class = OtpSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = create_otp_service(request.data['email'])

        #sending otp to the email
        subject = "OTP"
        context = {"otp": otp}
        # mail_template = "email/login_otp.html"
        # mail_shooter.delay(request.data['email'], subject, context, mail_template)
        return return_response(None, True, "OTP successfully sent to your email.!", status.HTTP_200_OK)


class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not settings.DEBUG:
            user = verify_otp_service(request.data)
        else:
            try:
                user = User.objects.get(email=request.data['email'])
            except User.DoesNotExist:
                raise ValidationError({"message": "User does not exist."})
        if not user or user is None:
            raise ValidationError({"message": "Wrong/expired otp..!"})

        data = get_tokens_for_user(user)
        return return_response(data, True, "Logged in Successfully", status.HTTP_200_OK)