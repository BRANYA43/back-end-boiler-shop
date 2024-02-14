from rest_framework.serializers import ModelSerializer

from orders import serializers
from utils.tests import CustomTestCase


class OrderProductCreateSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.OrderProductCreateSerializer

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['order', 'product', 'quantity']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)


class OrderCreateSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.OrderCreateSerializer

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['uuid', 'delivery', 'delivery_address', 'payment', 'comment']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)

    def test_uuid_field_is_read_only(self):
        field = self.get_serializer_field(self.serializer_class, 'uuid')
        self.assertTrue(field.read_only)

    def test_serializer_is_invalid_if_delivery_address_is_empty_when_delivery_is_different_from_pickup(self):
        serializer = self.serializer_class(data={'delivery': 'nova_post'})

        self.assertFalse(serializer.is_valid())

        expected_error = self.serializer_class.default_error_messages['invalid_delivery_address']
        self.assertEqual(serializer.errors['delivery'][0], expected_error)
