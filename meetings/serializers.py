# meetings/serializers.py

from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ["id", "faculty", "student", "date", "time", "status"]

class ApproveRejectMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ["status"]
