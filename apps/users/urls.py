from django.urls import path, include

from apps.users.views import sign_up

urlpatterns = [
    path('signup/', sign_up)
]
