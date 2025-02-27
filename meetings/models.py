# meetings/models.py

from django.db import models
from users.models import User

class Meeting(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faculty_meetings")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_meetings")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Meeting: {self.student.username} & {self.faculty.username} on {self.date} at {self.time} [{self.status}]"
