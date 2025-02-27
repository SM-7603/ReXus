# meetings/serializers.py

from rest_framework import serializers
from .models import Meeting
from users.models import User

class MeetingSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField()  # Faculty is shown as their username
    student = serializers.SerializerMethodField()  # Fetch full student details

    class Meta:
        model = Meeting
        fields = ["id", "faculty", "student", "date", "time", "status"]
        read_only_fields = ["status"]  # Status is set by faculty

    def get_student(self, obj):
        """Return full student details"""
        return {
            "id": obj.student.id,
            "username": obj.student.username,
            "email": obj.student.email
        }

class ApproveRejectMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ["status"]
