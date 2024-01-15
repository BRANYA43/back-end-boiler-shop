from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product, Specification


@receiver(post_save, sender=Product)
def create_specification_of_product(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'specification'):
        Specification.objects.create(product=instance)
