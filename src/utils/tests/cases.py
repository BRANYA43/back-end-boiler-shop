from typing import Type

from django.core.handlers.wsgi import WSGIRequest
from django.db import models
from django.test import RequestFactory
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.test import APITestCase

from utils.models import Image


class CustomTestCase(APITestCase):
    def tearDown(self) -> None:
        for image in Image.objects.all():
            image.image.delete()

    @staticmethod
    def get_fake_request() -> WSGIRequest:
        """
        Return fake request.
        """
        factory = RequestFactory()
        return factory.get('/')

    def get_fake_context(self) -> dict:
        """
        Return a fake context with a fake request by key 'request'.
        """
        return {'request': self.get_fake_request()}

    @staticmethod
    def get_meta_attr_of_model(model, name: str):
        """
        Return meta attribute of model by name.
        :param model: model class.
        :param name: attribute name.
        :return: Any
        """
        return getattr(model._meta, name)

    @staticmethod
    def get_model_field(model, name: str) -> Type[models.Field]:
        """
        Return model field by name.
        :param model: model class.
        :param name: field name.
        """
        return model._meta.get_field(name)

    @staticmethod
    def get_serializer_field(serializer, name: str) -> Type[serializers.Field]:
        """
        Return serializer field by name.
        :param serializer: serializer class.
        :param name: field name.
        """
        return serializer().fields[name]

    @staticmethod
    def get_serializer_field_names(serializer) -> list[str]:
        """
        Return list of serializer field names.
        :param serializer: serializer class.
        """
        return list(serializer().fields)

    def assertModelHasNecessaryFields(self, model, fields: list[str]):
        """
        Check that model has necessary field.
        :param model: model class.
        :param fields: list of model field names.
        """
        msg = "Model doesn't have some fields: {}."
        missed_fields = [field for field in fields if not hasattr(model, field)]
        self.assertFalse(missed_fields, msg.format(missed_fields))

    def assertSerializerHasOnlyExpectedFields(self, serializer, fields: list[str]):
        """
        Check that serializer have only expected fields.
        :param serializer: serializer class.
        :param fields: list of expected fields.
        """
        msg = "Serializer doesn't have some fields: {}."
        serializer_fields = self.get_serializer_field_names(serializer)
        missed_fields = [field for field in fields if field not in serializer_fields]
        self.assertFalse(missed_fields, msg.format(missed_fields))

    def assertStatusCodeEqual(self, response: Response, status_code: int):
        """
        Check that response status code is equal expected status code.
        :param response: response from client.
        :param status_code: expected status code.
        """
        msg = "Response status code isn't equal expected status code."
        self.assertEqual(response.status_code, status_code, msg)
