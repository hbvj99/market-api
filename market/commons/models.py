from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True


class BaseModel(TimeStampModel):
    class Meta:
        ordering = '-updated_at',
        abstract = True

    def save(self, *args, **kwargs):
        return super(BaseModel, self).save()

    def delete(self, *args, **kwargs):
        super(BaseModel, self).delete()
