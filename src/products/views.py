from rest_framework import viewsets

from products import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    http_method_names = ['get']
