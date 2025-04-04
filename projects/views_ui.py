# projects/views_ui.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ResearchProject

@login_required
def project_redirect_view(request):
    if request.user.role == "faculty":
        return redirect("faculty-projects-ui")
    elif request.user.role == "student":
        return redirect("student-projects-ui")
    return redirect("/")

@login_required
def faculty_projects_view(request):
    projects = request.user.faculty_projects.all()
    return render(request, "projects/faculty_projects.html", {"projects": projects})


@login_required
def student_projects_view(request):
    projects = request.user.student_projects.all()
    return render(request, "projects/my_project.html", {"projects": projects})
