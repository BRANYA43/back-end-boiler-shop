from rest_framework import viewsets

from products import serializers
from products.models import Category, Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_displayed=True)
    serializer_classes = {
        'list': serializers.ProductListSerializer,
        'retrieve': serializers.ProductDetailSerializer,
    }

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
