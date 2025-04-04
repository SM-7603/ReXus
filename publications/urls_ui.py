# publications/urls_ui.py

from django.urls import path
from .views_ui import publications_redirect_view

urlpatterns = [
    path("", publications_redirect_view, name="publications-ui"),
]
