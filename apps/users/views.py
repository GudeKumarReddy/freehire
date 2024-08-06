from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from apps.users.serializer import UserSerializer

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
    return return_response(data=None, success=True, message="User created successfully!", status_code=201)