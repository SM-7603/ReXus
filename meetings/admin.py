# meetings/admin.py

from django.contrib import admin
from .models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "faculty", "student", "date", "time", "status")
    list_filter = ("status",)
    search_fields = ("faculty__username", "student__username")
