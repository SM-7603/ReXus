# users/urls.py

from django.urls import path
from .views import RegisterUserView, LoginView, MeView, UserListView, dashboard_view, logout_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
    path('', UserListView.as_view(), name="user-list"),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),  # 👈 new route
]

