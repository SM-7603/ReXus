# projects/urls.py

from django.urls import path
from .views import (
    ResearchProjectListCreateView,
    ResearchProjectDetailView,
    AssignStudentView,
    RemoveStudentView
)

urlpatterns = [
    path('', ResearchProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ResearchProjectDetailView.as_view(), name='project-detail'),
    path('<int:project_id>/assign-student/', AssignStudentView.as_view(), name='assign-student'),
    path('<int:project_id>/remove-student/', RemoveStudentView.as_view(), name='remove-student'),
]

