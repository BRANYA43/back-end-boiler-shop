from uuid import uuid4

from django.utils.translation import gettext as _
from django.db import models


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
    )

    class Meta:
        abstract = True


class CreatedAndUpdatedDateTimeMixin(models.Model):
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))

    class Meta:
        abstract = True


class ImageSetMixin(UUIDMixin):
    from utils.models import Image

    images = models.ManyToManyField(Image, blank=True, verbose_name=_('Images'))

    class Meta:
        abstract = True
