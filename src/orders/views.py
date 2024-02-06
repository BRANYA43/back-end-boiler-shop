from rest_framework import viewsets

from orders import serializers
from orders.models import Order


# class OrderProductViewSet(viewsets.mixins.CreateModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     ...
#
# class CustomerViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.mixins.UpdateModelMixin, viewsets.GenericViewSet):
#     ...


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    http_method_names = ['get', 'post', 'patch']
