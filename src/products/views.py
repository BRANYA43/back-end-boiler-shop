from rest_framework import viewsets

from products import models, serializers


class ListRetrieveModelMixin(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin):
    pass


class ProductImageSetViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.ProductImageSet.objects.filter(product__is_displayed=True)
    serializer_class = serializers.ProductImageSetSerializer


class SpecificationViewSet(viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Specification.objects.filter(product__is_displayed=True)
    serializer_class = serializers.SpecificationSerializer


class ProductViewSet(ListRetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Product.objects.filter(is_displayed=True)
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(ListRetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
