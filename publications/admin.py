# publications/admin.py

from django.contrib import admin
from .models import Publication
from users.models import User

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "created_by", "created_at")
    list_filter = ("project", "created_by")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = User.objects.filter(role__in=["faculty", "admin"])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
