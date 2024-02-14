from rest_framework import mixins, viewsets
from rest_framework.response import Response

from orders.models import Order, OrderProduct
from orders import serializers


class OrderProductViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = serializers.OrderProductCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(status=response.status_code, headers=response.headers)


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(data={'uuid': response.data['uuid']}, status=response.status_code, headers=response.headers)
