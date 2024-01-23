from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order, Customer


@receiver(post_save, sender=Order)
def create_customer(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'customer'):
        Customer.objects.create(order=instance)
