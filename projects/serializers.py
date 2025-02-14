# projects/serializers.py

from rest_framework import serializers
from .models import ResearchProject
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ResearchProjectSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField()
    students = UserSerializer(many=True, required=False)  # ✅ Make students optional & show student details instead of just IDs

    class Meta:
        model = ResearchProject
        fields = ['id', 'title', 'description', 'faculty', 'students', 'start_date', 'end_date', 'status']

class AssignStudentSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()

    def validate_student_id(self, value):
        """Ensure student exists and is a valid user"""
        try:
            student = User.objects.get(id=value)
            if student.role != "student":
                raise serializers.ValidationError("Only students can be assigned.")
            return student
        except User.DoesNotExist:
            raise serializers.ValidationError("Student not found.")

