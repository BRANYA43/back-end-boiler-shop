from django.db import models

from utils.mixins import UUIDMixin, CreatedAndUpdatedDateTimeMixin


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
