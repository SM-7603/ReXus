# meetings/urls.py

from django.urls import path
from .views import MeetingListCreateView, ApproveMeetingView, RejectMeetingView
from .views_ui import meeting_redirect_view, faculty_meetings_view, student_meetings_view

# API endpoints
api_patterns = [
    path("api/", MeetingListCreateView.as_view(), name="meeting-list-create"),
    path("api/<int:pk>/approve/", ApproveMeetingView.as_view(), name="approve-meeting"),
    path("api/<int:pk>/reject/", RejectMeetingView.as_view(), name="reject-meeting"),
]

# UI templates
ui_patterns = [
    path("", meeting_redirect_view, name="meetings-redirect"),
    path("faculty/", faculty_meetings_view, name="faculty-meetings-ui"),
    path("my/", student_meetings_view, name="student-meetings-ui"),
]

urlpatterns = api_patterns + ui_patterns
