from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext as _

from orders.models import Order, OrderProduct


class OrderProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['order', 'product', 'quantity']


class OrderCreateSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'invalid': _('Invalid data. Expected a dictionary, but got {datatype}.'),
        'invalid_delivery_address': _('Delivery address cannot be empty if delivery way isn\'t "pickup".'),
    }

    class Meta:
        model = Order
        fields = ['uuid', 'delivery', 'delivery_address', 'payment', 'comment']
        read_only_fields = ['uuid']

    def validate_delivery(self, value):
        code = 'invalid_delivery_address'
        delivery = value
        delivery_address = self.initial_data.get('delivery_address')
        if delivery != Order.Delivery.PICKUP.lower() and not bool(delivery_address):
            raise ValidationError(self.default_error_messages[code], code)
        return value
