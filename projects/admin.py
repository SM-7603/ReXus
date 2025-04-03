# projects/admin.py

from django.contrib import admin
from .models import ResearchProject

@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "faculty")
    filter_horizontal = ("students",)
    search_fields = ("title",)
    list_filter = ("status",)
