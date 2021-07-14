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
