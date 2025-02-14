# users/urls.py

from django.urls import path
from .views import RegisterUserView, LoginView, MeView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
    path('', UserListView.as_view(), name="user-list"),
]

