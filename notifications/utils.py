# notifications/utils.py

import logging
from .tasks import send_email_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

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

def send_realtime_notification(user_id, payload):
    """Send a real-time WebSocket notification to a specific user"""
    try:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                "type": "send.notification",  # maps to `send_notification` in consumer
                "data": payload,
            }
        )
        logger.info(f"Sent real-time notification to user {user_id}")
    except Exception as e:
        logger.error(f"Error sending WebSocket notification to user {user_id}: {str(e)}")
