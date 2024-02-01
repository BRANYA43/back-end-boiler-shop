from decimal import Decimal

from rest_framework import serializers
from products.models import Category, Product, ProductImageSet, Specification


class ProductImageSetSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_image_url_list')

    class Meta:
        model = ProductImageSet
        fields = ['url', 'uuid', 'product', 'images']
        read_only_fields = ['uuid']

    @staticmethod
    def get_image_url_list(obj):
        return [image.image.url for image in obj.images.all()]


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    all_attributes = serializers.SerializerMethodField(method_name='get_all_attributes_as_dict')
    card_attributes = serializers.SerializerMethodField(method_name='get_card_attributes_as_list')
    detail_attributes = serializers.SerializerMethodField(method_name='get_detail_attributes_as_list')

    class Meta:
        model = Specification
        fields = ['url', 'uuid', 'product', 'all_attributes', 'card_attributes', 'detail_attributes']
        read_only_fields = ['uuid']

    @staticmethod
    def get_all_attributes_as_dict(obj):
        return {attribute.name: attribute.value for attribute in obj.all_attributes.all()}

    @staticmethod
    def get_card_attributes_as_list(obj):
        return [attribute.name for attribute in obj.card_attributes.all()]

    @staticmethod
    def get_detail_attributes_as_list(obj):
        return [attribute.name for attribute in obj.detail_attributes.all()]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.SerializerMethodField(method_name='get_decimal_price')

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

    @staticmethod
    def get_decimal_price(obj):
        if obj.price is not None:
            return obj.price.price
        return Decimal(0)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'uuid', 'name', 'parent', 'subs']
        read_only_fields = ['uuid']
