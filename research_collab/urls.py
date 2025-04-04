# research_collab/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import views as auth_views
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

    # UI views (templates / HTML responses)
    path('users/', include('users.urls')),  # for HTML pages
    # path('projects/', include('projects.ui_urls')), <- future addition for frontend dashboards

    path('api/users/', include('users.urls')),  
    path('api/projects/', include('projects.urls')),
    path('projects/', include('projects.urls')),
    path('api/meetings/', include('meetings.urls')),
    path('meetings/', include('meetings.urls')),
    path('api/publications/', include('publications.urls')),
    path('publications/', include('publications.urls_ui')),
    path('api/notifications/', include('notifications.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)