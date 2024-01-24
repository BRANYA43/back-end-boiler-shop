from django.db import models

from orders.validators import validate_phone
from products.models import Product, Price
from utils.mixins import UUIDMixin, CreatedAndUpdatedDateTimeMixin


class OrderProduct(UUIDMixin):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.ForeignKey(Price, on_delete=models.PROTECT, related_name='order_products', null=True, blank=True)

    def __str__(self):
        return str(self.product)

    @property
    def total_cost(self):
        return self.price.price * self.quantity


class PhoneField(models.CharField):
    default_validators = [validate_phone]

    def __init__(self, max_length=50, *args, **kwargs):
        super().__init__(max_length=max_length, *args, **kwargs)


class Customer(UUIDMixin):
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='customer')
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = PhoneField(null=True)

    def __str__(self):
        return str(self.full_name)


class Order(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    class Delivery(models.TextChoices):
        PICKUP = 'pickup', 'Pickup'
        NOVA_POST = 'nova_post', 'Nova post'

    class Payment(models.TextChoices):
        VISA = 'visa', 'Visa'
        MASTERCARD = 'mastercard', 'Mastercard'
        CASH_ON_DELIVERY = 'cash_on_delivery', 'Cash on delivery'

    class Status(models.TextChoices):
        IN_PROCESSING = 'in_processing', 'In processing'
        COMPLETED = 'completed', 'Completed'
        CANCELED = 'canceled', 'Canceled'

    delivery = models.CharField(max_length=50, choices=Delivery.choices, default=Delivery.PICKUP)
    delivery_address = models.CharField(max_length=255, null=True, blank=True)
    payment = models.CharField(max_length=50, choices=Payment.choices, default=Payment.CASH_ON_DELIVERY)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.IN_PROCESSING)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.uuid)

    @property
    def total_cost(self):
        return sum([order_product.total_cost for order_product in self.order_products.all()])
