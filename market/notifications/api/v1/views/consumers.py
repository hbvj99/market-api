import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        if self.scope["user"].is_anonymous:
            self.close()

        self.room_group_name = f'notification_group'
        if self.scope["user"]:
            self.room_name = f'notification_room_{self.scope["user"].id}'
        else:
            self.room_name = 'notification_room'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept('Token')  # Accept only protocol mentioned in header `Sec-WebSocket-Protocol`
        self.send(text_data=json.dumps({'status': f'connected to {self.room_group_name}'}))

    def receive(self, text_data):
        pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.close()

    def send_notification(self, event):
        if self.room_name == event.get('room_name'):
            self.send(text_data=json.dumps(event['value']))
