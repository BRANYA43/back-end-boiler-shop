import re

from rest_framework import serializers

from orders.models import Order, OrderProduct, Customer
from orders.validators import PHONE_PATTERN


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url', 'uuid', 'order', 'full_name', 'email', 'phone']
        read_only_fields = ['uuid']

    def validate_phone(self, phone):
        if phone and (match := re.match(PHONE_PATTERN, phone)) is not None:
            phone = '+38 ({}) {} {}-{}'.format(*match.groups()[1:])
        return phone


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['url', 'uuid', 'order', 'product', 'quantity', 'price', 'total_cost']
        read_only_fields = ['uuid', 'total_cost']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            'url',
            'uuid',
            'status',
            'payment',
            'is_paid',
            'delivery',
            'delivery_address',
            'total_cost',
            'updated',
            'created',
        ]
        read_only_fields = ['uuid', 'total_cost', 'updated', 'created']
