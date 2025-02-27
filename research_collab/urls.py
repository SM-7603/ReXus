# research_collab/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Welcome to the Research Collaboration API",
        "endpoints": {
            "Users": "/api/users/",
            "Projects": "/api/projects/",
            "Admin Panel": "/admin/",
        }
    })

urlpatterns = [
    path('', api_home, name="api-home"),  # Redirects `/` to API home
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  
    path('api/projects/', include('projects.urls')),
    path('api/meetings/', include('meetings.urls')),
]

