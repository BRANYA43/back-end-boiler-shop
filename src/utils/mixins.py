from uuid import uuid4

from django.db import models


class UUIDMixin(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True)

    class Meta:
        abstract = True


class CreatedAndUpdatedDateTimeMixin(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ImageSetMixin(UUIDMixin):
    from utils.models import Image

    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        abstract = True
