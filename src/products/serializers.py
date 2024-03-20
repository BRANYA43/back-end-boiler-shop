from rest_framework import serializers

from products.models import Category, Product


class ProductSerializerMixin(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_image_urls')
    cover_image = serializers.SerializerMethodField('get_cover_image_url')

    class Meta:
        model = Product
        fields = '__all__'

    def get_attributes(self, obj, name_field):
        return {attr.name: attr.value for attr in getattr(obj.specification, name_field).all()}

    def get_image_urls(self, obj):
        return [image.image.url for image in obj.image_set.images.all()]

    def get_cover_image_url(self, obj):
        if image := obj.image_set.cover_image:
            return image.image.url


class ProductListSerializer(ProductSerializerMixin):
    card_attributes = serializers.SerializerMethodField('get_card_attributes')

    class Meta:
        model = Product
        fields = ['uuid', 'category', 'name', 'price', 'stock', 'state', 'cover_image', 'images', 'card_attributes']

    def get_card_attributes(self, obj):
        return self.get_attributes(obj, 'all_attributes')


class ProductDetailSerializer(ProductSerializerMixin):
    all_attributes = serializers.SerializerMethodField('get_all_attributes')
    detail_attributes = serializers.SerializerMethodField('get_detail_attributes')

    class Meta:
        model = Product
        fields = [
            'uuid',
            'category',
            'name',
            'price',
            'stock',
            'state',
            'description',
            'cover_image',
            'images',
            'all_attributes',
            'detail_attributes',
        ]

    def get_all_attributes(self, obj):
        return self.get_attributes(obj, 'all_attributes')

    def get_detail_attributes(self, obj):
        return self.get_attributes(obj, 'detail_attributes')


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
        return [
            {'uuid': product.uuid, 'name': product.name} for product in obj.products.all().filter(is_displayed=True)
        ]
