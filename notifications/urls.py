# notifications/urls.py

from django.urls import path
from .views import TestNotificationView

urlpatterns = [
    path("test/", TestNotificationView.as_view(), name="test-notification"),
]
