from rest_framework.serializers import HyperlinkedModelSerializer

from orders.serializers import OrderSerializer, OrderProductSerializer
from utils.tests import CustomTestCase


class OrderProductSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = OrderProductSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'order', 'product', 'quantity', 'price', 'total_cost']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_total_cost_field(self):
        """
        Test:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'total_cost')
        self.assertTrue(field.read_only)


class OrderSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = OrderSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = [
            'url',
            'uuid',
            'status',
            'payment',
            'is_paid',
            'delivery',
            'delivery_address',
            'total_cost',
            'updated',
            'created',
        ]
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_total_cost_field(self):
        """
        Test:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'total_cost')
        self.assertTrue(field.read_only)
