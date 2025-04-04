# notifications/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import send_realtime_notification

class TestNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Send a test notification to the current user"""
        payload = {
            "message": f"Hello {request.user.username}, this is a test notification!",
            "type": "info"
        }
        send_realtime_notification(request.user.id, payload)
        return Response({"status": "notification sent"})
