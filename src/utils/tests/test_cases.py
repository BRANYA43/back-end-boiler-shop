from django.db import models
from rest_framework import serializers

from utils.tests import CustomTestCase


class TestModel(models.Model):
    field_1 = models.Field()
    field_2 = models.Field()
    field_3 = models.Field()

    class Meta:
        abstract = True


class TestSerializer(serializers.Serializer):
    field_1 = serializers.Field()
    field_2 = serializers.Field()


class TestCaseTest(CustomTestCase):
    def test_get_meta_attr_of_model(self):
        attr = self.get_meta_attr_of_model(TestModel, 'abstract')
        self.assertTrue(attr)

    def test_get_model_field_method_returns_correct_field(self):
        field = self.get_model_field(TestModel, 'field_1')
        self.assertIsInstance(field, models.Field)

    def test_get_model_field_name_method_returns_correct_field_names(self):
        fields = self.get_model_field_names(TestModel)
        expected_fields = ['field_1', 'field_2', 'field_3']
        self.assertListEqual(fields, expected_fields)

    def test_get_serializer_field_method_returns_correct_field(self):
        field = self.get_serializer_field(TestSerializer, 'field_1')
        self.assertIsInstance(field, serializers.Field)

    def test_get_serializer_field_names_method_returns_correct_field_names(self):
        fields = self.get_serializer_field_names(TestSerializer)
        expected_fields = ['field_1', 'field_2']
        self.assertListEqual(fields, expected_fields)

    def test_assertModelHasNecessaryFields_doesnt_raise_error(self):
        necessary_fields = ['field_3', 'field_2']
        self.assertModelHasNecessaryFields(TestModel, necessary_fields)

    def test_assertModelHasNecessaryFields_raises_error(self):
        with self.assertRaises(AssertionError):
            self.assertModelHasNecessaryFields(TestModel, ['none_field'])

    def test_assertSerializerHasOnlyExpectedFields_doesnt_raise_error(self):
        expected_fields = ['field_2', 'field_1']
        self.assertSerializerHasOnlyExpectedFields(TestSerializer, expected_fields)

    def test_assertSerializerHasOnlyExpectedFields_raises_error(self):
        with self.assertRaises(AssertionError):
            self.assertSerializerHasOnlyExpectedFields(TestSerializer, ['none_field'])
