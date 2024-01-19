from rest_framework import serializers

from products.models import Category, Product, Specification


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
            'grade',
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
