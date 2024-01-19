from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'uuid', 'name', 'parent', 'subs']
        read_only_fields = ['uuid']
