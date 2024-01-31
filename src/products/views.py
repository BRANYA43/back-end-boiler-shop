from rest_framework import viewsets

from products import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.filter(is_displayed=True)
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    http_method_names = ['get']
