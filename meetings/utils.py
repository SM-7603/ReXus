# meetings/utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_meeting_notification_email(subject, message, recipient_email):
    """
    Send an email notification to a recipient (student/faculty).
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False
    )
