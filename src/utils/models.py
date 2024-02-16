from django.db import models
from django.utils.translation import gettext as _

from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin
from utils.utils import get_upload_filename


class Image(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Title'))
    image = models.ImageField(upload_to=get_upload_filename, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.name


class Attribute(UUIDMixin):
    name = models.CharField(max_length=100, verbose_name=_('Title'))
    value = models.CharField(max_length=100, verbose_name=_('Value'))

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')

    def __str__(self):
        return f'{self.name}: {self.value}'
