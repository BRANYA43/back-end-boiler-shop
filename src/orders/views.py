from rest_framework import viewsets

from orders import serializers
from orders.models import Order, Customer


class CustomerViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    http_method_names = ['get', 'patch']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    http_method_names = ['get', 'post', 'patch']
