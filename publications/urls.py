# publications/urls.py

from django.urls import path
from .views import PublicationListCreateView, PublicationDetailView
from .views_ui import publications_redirect_view

urlpatterns = [
    path('', PublicationListCreateView.as_view(), name='publication-list-create'),
    path('<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]

urlpatterns += [
    path("", publications_redirect_view, name="publications-ui"),
]