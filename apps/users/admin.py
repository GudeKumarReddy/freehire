from django.contrib import admin

from apps.users.models import User, OTP


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'is_18_plus', 'gender', 'is_staff']


admin.site.register(User, UserAdmin)
admin.site.register(OTP)
