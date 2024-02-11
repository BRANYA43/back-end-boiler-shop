from rest_framework import viewsets

from orders import serializers
from orders.models import Order, Customer, OrderProduct


class OrderProductViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = serializers.OrderProductSerializer


class CustomerViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class OrderViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
