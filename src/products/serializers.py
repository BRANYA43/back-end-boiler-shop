from rest_framework import serializers

from products.models import Category, Product, ProductImageSet, Specification, Price


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['url', 'uuid', 'product', 'price', 'created']
        read_only_fields = ['uuid']


class ProductImageSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImageSet
        fields = ['url', 'uuid', 'product', 'images']
        read_only_fields = ['uuid']


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specification
        fields = ['url', 'uuid', 'product', 'attributes']
        read_only_fields = ['uuid']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'url',
            'uuid',
            'category',
            'name',
            'slug',
            'price',
            'stock',
            'description',
            'is_displayed',
            'specification',
            'image_set',
            'updated',
            'created',
        ]
        read_only_fields = ['uuid', 'updated', 'created']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'uuid', 'name', 'parent', 'subs']
        read_only_fields = ['uuid']
