import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from utils.models import Image


@receiver(pre_delete, sender=Image)
def delete_image_file(sender, instance, *args, **kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)
