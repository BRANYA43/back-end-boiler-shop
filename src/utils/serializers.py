from rest_framework import serializers


class ReadOnlyHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields: list[str] = []
        read_only_fields = fields
