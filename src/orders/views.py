from rest_framework import mixins, viewsets
from rest_framework.response import Response

from orders.models import Order, OrderProduct, Customer
from orders import serializers


class CreateViewSetMixin(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if kwargs.get('save_temp_data'):
            self.temp_data = response.data
        return Response(status=response.status_code, headers=response.headers)


class CustomerViewSet(CreateViewSetMixin):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerCreateSerializer


class OrderProductViewSet(CreateViewSetMixin):
    queryset = OrderProduct.objects.all()
    serializer_class = serializers.OrderProductCreateSerializer


class OrderViewSet(CreateViewSetMixin):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        kwargs['save_temp_data'] = True
        response = super().create(request, *args, **kwargs)
        response.data = {'uuid': self.temp_data['uuid']}
        del self.temp_data
        return response
