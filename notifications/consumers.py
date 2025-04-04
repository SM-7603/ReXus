# notifications/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Temporarily allow unauthenticated users to test notifications"""
        self.user_group = f"user_{self.scope.get('url_route', {}).get('kwargs', {}).get('user_id', 'anonymous')}"
        await self.channel_layer.group_add(self.user_group, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Remove user from notification group on disconnect"""
        await self.channel_layer.group_discard(self.user_group, self.channel_name)

    async def receive(self, text_data):
        """Echo test messages — purely for manual dev testing"""
        await self.send(text_data=json.dumps({
            "message": "Echo from server!",
        }))

    async def send_notification(self, event):
        """Send structured notification payload to WebSocket"""
        await self.send(text_data=json.dumps(event["data"]))
