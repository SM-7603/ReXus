# projects/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ResearchProject
from .serializers import ResearchProjectSerializer, AssignStudentSerializer
from users.models import User

class ResearchProjectListCreateView(generics.ListCreateAPIView):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer

    def perform_create(self, serializer):
        """Ensure only faculty can create projects"""
        if not self.request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        if not hasattr(self.request.user, "role") or self.request.user.role != "faculty":
            return Response({"error": "Only faculty can create projects"}, status=status.HTTP_403_FORBIDDEN)

        serializer.save(faculty=self.request.user)

class ResearchProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer

class AssignStudentView(APIView):
    """API to assign a student to a project (Faculty Only)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, project_id):
        try:
            project = ResearchProject.objects.get(id=project_id)
        except ResearchProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user.role != "faculty":
            return Response({"error": "Only faculty can assign students"}, status=status.HTTP_403_FORBIDDEN)

        serializer = AssignStudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data["student_id"]
            project.assign_student(student)
            return Response({"message": "Student assigned successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveStudentView(APIView):
    """API to remove a student from a project (Faculty Only)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, project_id):
        try:
            project = ResearchProject.objects.get(id=project_id)
        except ResearchProject.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user.role != "faculty":
            return Response({"error": "Only faculty can remove students"}, status=status.HTTP_403_FORBIDDEN)

        serializer = AssignStudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data["student_id"]
            project.remove_student(student)
            return Response({"message": "Student removed successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

