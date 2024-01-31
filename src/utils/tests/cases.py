import os
import shutil
from pathlib import Path
from typing import Type

from django.conf import settings
from django.db import models
from rest_framework import serializers
from rest_framework.test import APITestCase


class CustomTestCase(APITestCase):
    def tearDown(self) -> None:
        images_path = Path(settings.MEDIA_ROOT, 'images/')
        if images_path.exists():
            shutil.rmtree(images_path)
            os.makedirs(images_path)

    @staticmethod
    def get_meta_attr_of_model(model: Type[models.Model], name: str):
        return getattr(model._meta, name)

    @staticmethod
    def get_model_field(model: Type[models.Model], name: str) -> Type[models.Field]:
        return model._meta.get_field(name)

    @staticmethod
    def get_serializer_field(serializer: Type[serializers.Serializer], name: str) -> Type[serializers.Field]:
        return serializer().fields[name]

    @staticmethod
    def get_serializer_field_names(serializer: Type[serializers.Serializer]) -> list[str]:
        return list(serializer().fields)

    def assertModelHasNecessaryFields(self, model: Type[models.Model], necessary_fields: list[str]):
        for field in necessary_fields:
            self.assertTrue(hasattr(model, field))

    def assertSerializerHasOnlyExpectedFields(
        self, serializer: Type[serializers.Serializer], expected_fields: list[str]
    ):
        serializer_fields = self.get_serializer_field_names(serializer)
        serializer_fields.sort()
        expected_fields.sort()

        self.assertListEqual(serializer_fields, expected_fields)

    def assertStatusCodeEqual(self, response, status_code, msg=None):
        self.assertEqual(response.status_code, status_code, msg=msg)
