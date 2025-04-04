# users/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer

# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # public access...

    def perform_create(self, serializer):
        serializer.save() # let serializer handle the hashing

# User list view - to view all users for faculties / admin
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# User Login View (JWT)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            })
        return Response({"error": "Invalid credentials"}, status=400)

# Get Current Logged-in User
class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

@login_required
def dashboard_view(request):
    """Redirect to a dashboard template based on user role"""
    role = request.user.role
    if role == "student":
        return render(request, "dashboards/student.html")
    elif role == "faculty":
        return render(request, "dashboards/faculty.html")
    elif role == "admin":
        return redirect("/admin/")
    else:
        return redirect("/")

def logout_view(request):
    """logout view"""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/")
