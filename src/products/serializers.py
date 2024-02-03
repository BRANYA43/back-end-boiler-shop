from decimal import Decimal

from rest_framework import serializers
from products.models import Category, Product, ProductImageSet, Specification
from utils.serializers import ReadOnlyHyperlinkedModelSerializer


class ProductImageSetSerializer(ReadOnlyHyperlinkedModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_image_url_list')

    class Meta:
        model = ProductImageSet
        fields = ['url', 'uuid', 'product', 'images']

    @staticmethod
    def get_image_url_list(obj):
        return [image.image.url for image in obj.images.all()]


class SpecificationSerializer(ReadOnlyHyperlinkedModelSerializer):
    all_attributes = serializers.SerializerMethodField(method_name='get_all_attribute_items')
    card_attributes = serializers.SerializerMethodField(method_name='get_card_attribute_names')
    detail_attributes = serializers.SerializerMethodField(method_name='get_detail_attribute_names')

    class Meta:
        model = Specification
        fields = ['url', 'uuid', 'product', 'all_attributes', 'card_attributes', 'detail_attributes']

    @staticmethod
    def get_all_attribute_items(obj) -> dict:
        return {attribute.name: attribute.value for attribute in obj.all_attributes.all()}

    @staticmethod
    def get_card_attribute_names(obj) -> list[str]:
        return [attribute.name for attribute in obj.card_attributes.all()]

    @staticmethod
    def get_detail_attribute_names(obj) -> list[str]:
        return [attribute.name for attribute in obj.detail_attributes.all()]


class ProductSerializer(ReadOnlyHyperlinkedModelSerializer):
    price_value = serializers.SerializerMethodField(method_name='get_price_value')

    class Meta:
        model = Product
        fields = [
            'url',
            'uuid',
            'category',
            'name',
            'slug',
            'price',
            'price_value',
            'stock',
            'description',
            'specification',
            'image_set',
            'is_displayed',
            'updated',
            'created',
        ]

    @staticmethod
    def get_price_value(obj):
        return Decimal(0) if obj.price is None else obj.price.value


class CategorySerializer(ReadOnlyHyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'uuid', 'name', 'parent', 'subs']
