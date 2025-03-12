# notifications/utils.py

from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email_notification(subject, message, recipient_list):
    """Send email notifications with error handling."""
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
        logger.info(f"Email sent to: {recipient_list}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {recipient_list}: {str(e)}")
        return False
