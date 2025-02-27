# meetings/urls.py

from django.urls import path
from .views import MeetingListCreateView, ApproveMeetingView, RejectMeetingView

urlpatterns = [
    path("", MeetingListCreateView.as_view(), name="meeting-list"),
    path("<int:pk>/approve/", ApproveMeetingView.as_view(), name="approve-meeting"),
    path("<int:pk>/reject/", RejectMeetingView.as_view(), name="reject-meeting"),
]
