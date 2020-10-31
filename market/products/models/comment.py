from django.contrib.auth import get_user_model
from django.db import models

from market.commons.models import BaseModel
from ..models.product import Product

User = get_user_model()


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    reply = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.content

    def comment_count(self):
        return self.content.count()
