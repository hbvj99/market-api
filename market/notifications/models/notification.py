import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from django.db import models

from market.commons.models import BaseModel

User = get_user_model()

USER = 'user'
PRODUCT = 'product'
COMMENT = 'comment'
ENTITY_TYPE = [
    (USER, 'user'),
    (PRODUCT, 'product'),
    (COMMENT, 'comment')
]


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    is_seen = models.BooleanField(default=False)
    entity_type = models.CharField(max_length=150, choices=ENTITY_TYPE, blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.description:
            channel_layer = get_channel_layer()
            data = {'user': self.user.id, 'description': self.description}
            async_to_sync(channel_layer.group_send)(
                'notification_group',
                {
                    'type': 'send_notification',
                    'room_name': f'notification_room_{self.user.id}',
                    'value': json.dumps(data)
                }
            )
        super(Notification, self).save(*args, **kwargs)
