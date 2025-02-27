# meetings/views.py

from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Meeting
from .serializers import MeetingSerializer, ApproveRejectMeetingSerializer

class MeetingListCreateView(generics.ListCreateAPIView):
    """List all meetings (GET) & allow students to request new meetings (POST)"""
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        """Return meetings relevant to the user"""
        user = self.request.user
        if user.role == "faculty":
            return Meeting.objects.filter(faculty=user)  # Faculty sees their meetings
        elif user.role == "student":
            return Meeting.objects.filter(student=user)  # Students see only their meetings
        return Meeting.objects.none()  # No role, no access

    def perform_create(self, serializer):
        """Ensure only students can request meetings"""
        if self.request.user.role != "student":
            raise serializers.ValidationError("Only students can request meetings")
        serializer.save(student=self.request.user)

class ApproveMeetingView(APIView):
    """Approve a meeting (faculty only)"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            meeting = Meeting.objects.get(pk=pk, faculty=request.user)
            serializer = ApproveRejectMeetingSerializer(meeting, data={"status": "approved"}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Meeting approved successfully"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Meeting.DoesNotExist:
            return Response({"error": "Meeting not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)

class RejectMeetingView(APIView):
    """Reject a meeting (faculty only)"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            meeting = Meeting.objects.get(pk=pk, faculty=request.user)
            serializer = ApproveRejectMeetingSerializer(meeting, data={"status": "rejected"}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Meeting rejected successfully"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Meeting.DoesNotExist:
            return Response({"error": "Meeting not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)
