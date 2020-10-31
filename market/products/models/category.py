from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...commons.models import BaseModel


class Category(BaseModel):
    name = models.CharField(_('name'), max_length=90, blank=False)
    code = models.CharField(_('code'), max_length=110, blank=False)
