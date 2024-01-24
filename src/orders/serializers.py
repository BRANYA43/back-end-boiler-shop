from rest_framework import serializers

from orders.models import Order


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
