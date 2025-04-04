# projects/urls.py

from django.urls import path
from .views import (
    ResearchProjectListCreateView,
    ResearchProjectDetailView,
    AssignStudentView,
    RemoveStudentView
)
from .views_ui import faculty_projects_view, student_projects_view, project_redirect_view

# API URLs
api_patterns = [
    path("api/", ResearchProjectListCreateView.as_view(), name='project-list-create'),
    path("api/<int:pk>/", ResearchProjectDetailView.as_view(), name='project-detail'),
    path("api/<int:project_id>/assign-student/", AssignStudentView.as_view(), name='assign-student'),
    path("api/<int:project_id>/remove-student/", RemoveStudentView.as_view(), name='remove-student'),
]

# UI Pages
ui_patterns = [
    path("", project_redirect_view, name="projects-redirect"),
    path("faculty/", faculty_projects_view, name="faculty-projects-ui"),
    path("my/", student_projects_view, name="student-projects-ui"),
]

urlpatterns = api_patterns + ui_patterns
