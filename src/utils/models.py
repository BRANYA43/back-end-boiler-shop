from django.db import models

from utils.mixins import UUIDMixin


class Attribute(UUIDMixin):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}: {self.value}'
