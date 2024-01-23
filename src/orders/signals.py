from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from orders.models import Order, Customer, OrderProduct


@receiver(pre_save, sender=OrderProduct)
def set_order_product_price(sender, instance, *args, **kwargs):
    if instance.price is None:
        instance.price = instance.product.price


@receiver(post_save, sender=Order)
def create_customer(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'customer'):
        Customer.objects.create(order=instance)
