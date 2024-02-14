import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext as _

from orders.models import Order, OrderProduct, Customer
from orders.validators import PHONE_PATTERN


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['order', 'full_name', 'email', 'phone']

    def validate_phone(self, value):
        if value and (match := re.match(PHONE_PATTERN, value)) is not None:
            value = '+38 ({}) {} {}-{}'.format(*match.groups()[1:])
        return value


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
