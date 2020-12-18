from cuser.fields import CurrentUserField
from django.db import models
from django.utils import timezone


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(editable=False, null=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True


class CuserModel(models.Model):
    created_by = CurrentUserField(
        add_only=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
        null=True
    )

    updated_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        abstract = True


class BaseModel(CuserModel, TimeStampModel):
    class Meta:
        ordering = '-updated_at',
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()
