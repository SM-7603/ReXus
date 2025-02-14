# projects/models.py

from django.db import models
from users.models import User

class ResearchProject(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faculty_projects", limit_choices_to={'role': 'faculty'})
    students = models.ManyToManyField(User, related_name="student_projects", limit_choices_to={'role': 'student'})
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def assign_student(self, student):
        """Assign a student to the project"""
        if student.role == "student":
            self.students.add(student)

    def remove_student(self, student):
        """Remove a student from the project"""
        if student in self.students.all():
            self.students.remove(student)

    def __str__(self):
        return self.title

