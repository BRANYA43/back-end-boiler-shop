from rest_framework import viewsets

from orders import serializers
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    http_method_names = ['get', 'post', 'patch']
