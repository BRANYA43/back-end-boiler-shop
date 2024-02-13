from rest_framework import serializers

from products.models import Category


class FilterListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecurseSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    children = RecurseSerializer(many=True)

    class Meta:
        list_serializer_class = FilterListSerializer
        model = Category
        fields = ['uuid', 'name', 'image', 'parent', 'children']


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Category
        fields = ['uuid', 'name', 'image', 'parent', 'children', 'products']

    def get_children(self, obj):
        return [{'uuid': child.uuid, 'name': child.name} for child in obj.children.all()]

    def get_products(self, obj):
        return [{'uuid': product.uuid, 'name': product.name} for product in obj.products.all()]
