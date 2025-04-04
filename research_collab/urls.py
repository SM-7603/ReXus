# research_collab/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def api_home(request):
    return JsonResponse({
        "message": "Welcome to the Research Collaboration API",
        "endpoints": {
            "Users": "/api/users/",
            "Projects": "/api/projects/",
            "Meetings": "/api/meetings/",
            "Publications": "/api/publications/",
            "Notifications": "/api/notifications/",
            "Admin Panel": "/admin/",
        }
    })

urlpatterns = [
    path('', api_home, name="api-home"),  # Redirects `/` to API home
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  
    path('api/projects/', include('projects.urls')),
    path('api/meetings/', include('meetings.urls')),
    path('api/publications/', include('publications.urls')),
    path('api/notifications/', include('notifications.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)