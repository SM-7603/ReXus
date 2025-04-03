# publications/models.py

from django.db import models
from users.models import User
from projects.models import ResearchProject

class Publication(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    doi = models.CharField(max_length=100, blank=True, null=True)  # Optional DOI
    co_authors = models.TextField(blank=True, help_text="Comma-separated list of co-authors")
    publication_date = models.DateField(blank=True, null=True)

    file = models.FileField(upload_to='publications/', blank=True, null=True)

    # Relationships
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE, related_name='publications')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.created_by.username}"
