from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from products import serializers
from products.filters import ProductFilter
from products.models import Category, Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_displayed=True)
    serializer_classes = {
        'list': serializers.ProductListSerializer,
        'retrieve': serializers.ProductDetailSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        return self.serializer_classes[self.action]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_classes = {
        'list': serializers.CategoryListSerializer,
        'retrieve': serializers.CategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]
