from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin
from utils.utils import get_upload_filename


class Image(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to=get_upload_filename)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Attribute(UUIDMixin):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        pass

    def __str__(self):
        return f'{self.name}: {self.value}'
