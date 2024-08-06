from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_18_plus', 'gender', 'is_staff']


admin.site.register(User, UserAdmin)
