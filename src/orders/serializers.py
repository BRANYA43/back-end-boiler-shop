import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext as _

from orders.models import Order, OrderProduct, Customer
from orders.validators import PHONE_PATTERN


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone']

    def validate_phone(self, value):
        if value and (match := re.match(PHONE_PATTERN, value)) is not None:
            value = '+38 ({}) {} {}-{}'.format(*match.groups()[1:])
        return value


class OrderProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


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


class OrderSetCreateSerializer(serializers.Serializer):
    order = OrderCreateSerializer(required=True)
    customer = CustomerCreateSerializer(required=True)
    products = OrderProductCreateSerializer(required=True, many=True)

    class Meta:
        fields = ['order', 'customer', 'products']

    def create(self, validated_data):
        order_data = validated_data.pop('order')
        customer_data = validated_data.pop('customer')
        products_data = validated_data.pop('products')

        order = self._create_order(order_data)
        customer = self._create_customer(order, customer_data)
        products = [self._create_products(order, data) for data in products_data]

        return {'order': order, 'customer': customer, 'products': products}

    def _create_order(self, data):
        return self._create_model_instance(Order, data)

    def _create_customer(self, order, data):
        data['order'] = order
        return self._create_model_instance(Customer, data)

    def _create_products(self, order, data):
        data['order'] = order
        return self._create_model_instance(OrderProduct, data)

    @staticmethod
    def _create_model_instance(model, data):
        instance = model(**data)
        instance.full_clean()
        instance.save()
        return instance
