from rest_framework import serializers

from utils.models import Attribute


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ['url', 'uuid', 'uuid', 'name', 'value']
        read_only_fields = ['uuid']
