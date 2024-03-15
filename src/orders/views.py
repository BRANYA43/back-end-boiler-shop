from rest_framework import viewsets, status
from rest_framework.response import Response

from orders import serializers


class OrderSetViewSet(viewsets.ViewSet):
    serializer_class = serializers.OrderSetCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
