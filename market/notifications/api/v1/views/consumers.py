import json
from urllib.parse import parse_qs

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        query_params = parse_qs(self.scope["query_string"].decode())
        user = query_params.get('user')

        self.room_group_name = f'notification_group'
        if user:
            self.room_name = f'notification_room_{user[0]}'
        else:
            self.room_name = 'notification_room'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': f'connected to {self.room_group_name}'}))

    def receive(self, text_data):
        pass

    def disconnect(self, close_code):
        self.close()

    def send_notification(self, event):
        if self.room_name == event.get('room_name'):
            self.send(text_data=json.dumps(event['value']))
