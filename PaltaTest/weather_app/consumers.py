from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from .models import Clients


class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        c = Clients.objects.get(channel_name=self.channel_name)
        c.channel_name = None
        c.save()
        self.close()

    def receive(self, text_data):
        user_id = text_data
        channel = {
            'channel_name': self.channel_name,
            'user_id': user_id
        }

        Clients.objects.update_or_create(defaults=channel, user_id=user_id)

    def events_alarm(self, event):
        if event['channel_name'] == self.channel_name:
            self.send_json(
                {
                    'type': 'alarm',
                    'content': event['content']
                }
            )

    def channel_alarm(self, channel):
        self.send_json(
            {
                'type': 'channel',
                'content': channel['content']
            }
        )
