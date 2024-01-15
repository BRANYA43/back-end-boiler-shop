from typing import Type

from django.db.models import Field, Model
from rest_framework.serializers import Serializer
from rest_framework.test import APITestCase


class CustomTestCase(APITestCase):
    @staticmethod
    def get_meta_attr_of_model(model: Type[Model], name: str):
        return getattr(model._meta, name)

    @staticmethod
    def get_model_field(model: Type[Model], name: str) -> Type[Field]:
        return model._meta.get_field(name)

    @staticmethod
    def get_model_field_names(model: Type[Model]) -> list[str]:
        return [field.name for field in model._meta.fields]

    @staticmethod
    def get_serializer_field(serializer: Type[Serializer], name: str) -> Type[Field]:
        return serializer().fields[name]

    @staticmethod
    def get_serializer_field_names(serializer: Type[Serializer]) -> list[str]:
        return list(serializer().fields)

    def assertModelHasNecessaryFields(self, model: Type[Model], necessary_fields: list[str]):
        for field in necessary_fields:
            self.assertTrue(hasattr(model, field))

    def assertSerializerHasOnlyExpectedFields(self, serializer: Type[Serializer], expected_fields: list[str]):
        serializer_fields = self.get_serializer_field_names(serializer)
        serializer_fields.sort()
        expected_fields.sort()

        self.assertListEqual(serializer_fields, expected_fields)
