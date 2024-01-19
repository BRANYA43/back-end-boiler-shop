from rest_framework import serializers

from utils.models import Attribute, Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'uuid', 'name', 'image', 'updated', 'created']
        read_only_fields = ['uuid', 'updated', 'created']


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ['url', 'uuid', 'uuid', 'name', 'value']
        read_only_fields = ['uuid']
