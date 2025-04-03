# publications/views.py

from rest_framework import generics, permissions
from .models import Publication
from .serializers import PublicationSerializer

class PublicationListCreateView(generics.ListCreateAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "faculty":
            return Publication.objects.filter(created_by=user)
        elif user.role == "student":
            return Publication.objects.filter(project__students=user)
        elif user.role == "admin":
            return Publication.objects.all()
        return Publication.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != "faculty":
            raise PermissionError("Only faculty can upload publications.")
        serializer.save(created_by=self.request.user)

class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Publication.objects.all()
