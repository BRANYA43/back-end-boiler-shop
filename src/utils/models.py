from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin


class Image(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.SlugField(max_length=50, unique=True)
    image = models.ImageField()

    class Meta:
        pass

    def __str__(self):
        return self.name


class Attribute(UUIDMixin):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}: {self.value}'
