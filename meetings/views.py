# meetings/views.py

from rest_framework import generics, permissions
from .models import Meeting
from .serializers import MeetingSerializer

class MeetingListCreateView(generics.ListCreateAPIView):
    """List all meetings (GET) & allow students to request new meetings (POST)"""
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        """Return meetings relevant to the user"""
        user = self.request.user
        if user.role == "faculty":
            return Meeting.objects.filter(faculty=user)
        elif user.role == "student":
            return Meeting.objects.filter(student=user)
        return Meeting.objects.none()

    def perform_create(self, serializer):
        """Ensure only students can request meetings"""
        if self.request.user.role != "student":
            raise serializers.ValidationError("Only students can request meetings")
        serializer.save(student=self.request.user)
