# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "username", "email", "role", "is_staff", "is_superuser", "date_joined")
    list_filter = ("role", "is_staff")
    search_fields = ("username", "email")
