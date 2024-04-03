from django.utils.translation import gettext as _

from decimal import Decimal

from django.core import validators
from django.db import models

from orders.validators import validate_phone, validate_name
from products.models import Product, Price
from utils.mixins import UUIDMixin, CreatedAndUpdatedDateTimeMixin


class OrderProduct(UUIDMixin):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE, related_name='products', verbose_name=_('Order'))
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='order_products', verbose_name=_('Product')
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[validators.MinValueValidator(1)], verbose_name=_('Quantity')
    )
    price = models.ForeignKey(
        to=Price,
        on_delete=models.PROTECT,
        related_name='order_products',
        null=True,
        blank=True,
        verbose_name=_('Price'),
    )

    class Meta:
        verbose_name = _('Order Product')
        verbose_name_plural = _('Order Products')

    def __str__(self):
        return str(self.product)

    @property
    def total_cost(self) -> Decimal:
        return self.price.value * self.quantity


class PhoneField(models.CharField):
    default_validators = [validate_phone]

    def __init__(self, max_length=50, *args, **kwargs):
        super().__init__(max_length=max_length, *args, **kwargs)


class Customer(UUIDMixin):
    order = models.OneToOneField(to='Order', on_delete=models.CASCADE, related_name='customer', verbose_name=_('Order'))
    full_name = models.CharField(
        max_length=100,
        validators=[validators.MinLengthValidator(3), validate_name],
        verbose_name=_('Full Name'),
    )
    email = models.EmailField(verbose_name=_('Email'))
    phone = PhoneField(verbose_name=_('Phone'))

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return str(self.full_name)


class Order(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    class Delivery(models.TextChoices):
        PICKUP = 'pickup', _('Pickup')
        NOVA_POST = 'nova_post', _('Nova post')

    class Payment(models.TextChoices):
        VISA = 'visa', _('Visa')
        MASTERCARD = 'mastercard', _('Mastercard')
        CASH_ON_DELIVERY = 'cash_on_delivery', _('Cash on delivery')

    class Status(models.TextChoices):
        IN_PROCESSING = 'in_processing', _('In processing')
        COMPLETED = 'completed', _('Completed')
        CANCELED = 'canceled', _('Canceled')

    delivery = models.CharField(
        max_length=50, choices=Delivery.choices, default=Delivery.PICKUP, verbose_name=_('Delivery Way')
    )
    delivery_address = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Delivery Address'))
    payment = models.CharField(
        max_length=50, choices=Payment.choices, default=Payment.CASH_ON_DELIVERY, verbose_name=_('Payment')
    )
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.IN_PROCESSING, verbose_name=_('Status')
    )
    comment = models.TextField(null=True, blank=True, verbose_name=_('Comment'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.uuid)

    @property
    def total_cost(self) -> Decimal:
        return sum([product.total_cost for product in self.products.all()])

    def get_payment_name(self):
        return dict(self.Payment.choices)[self.payment]
