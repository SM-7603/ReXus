# publications/views_ui.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def publications_redirect_view(request):
    if request.user.role == "faculty":
        return render(request, "publications/faculty_publications.html")
    return render(request, "publications/student_publications.html")
