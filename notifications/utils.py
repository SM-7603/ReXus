# notifications/utils.py

import logging
from .tasks import send_email_task

logger = logging.getLogger(__name__)

def send_email_notification(subject, message, recipient_list):
    """Trigger async email notification with logging."""
    try:
        send_email_task.delay(subject, message, recipient_list)
        logger.info(f"Email task triggered for: {recipient_list}")
        return True
    except Exception as e:
        logger.error(f"Failed to trigger email task for {recipient_list}: {str(e)}")
        return False
