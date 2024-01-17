from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product, ProductImageSet, Specification


@receiver(post_save, sender=Product)
def create_specification_of_product(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'specification'):
        Specification.objects.create(product=instance)


@receiver(post_save, sender=Product)
def create_product_image_set(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'image_set'):
        ProductImageSet.objects.create(product=instance)
