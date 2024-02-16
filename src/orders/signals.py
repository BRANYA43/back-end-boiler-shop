from django.db.models.signals import pre_save
from django.dispatch import receiver

from orders.models import OrderProduct


@receiver(pre_save, sender=OrderProduct)
def set_order_product_price(sender, instance, *args, **kwargs):
    if instance.price is None:
        instance.price = instance.product.prices.latest('created')
