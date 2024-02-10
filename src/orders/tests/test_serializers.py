from unittest.mock import MagicMock

from rest_framework.serializers import HyperlinkedModelSerializer

from orders.serializers import OrderSerializer, OrderProductSerializer, CustomerSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order, create_test_order_product, create_test_product


class CustomerSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = CustomerSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'order', 'full_name', 'email', 'phone']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_serializer_validates_and_formats_phone(self):
        valid_phones = [
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '380501234567',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
        ]
        expected_phone = '+38 (050) 123 45-67'

        customer = create_test_order().customer

        for phone in valid_phones:
            serializer = self.serializer(
                instance=customer, data={'phone': phone}, context={'request': MagicMock()}, partial=True
            )
            serializer.is_valid()
            self.assertEqual(serializer.validated_data['phone'], expected_phone)


class OrderProductSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = OrderProductSerializer
        self.context = {'request': MagicMock()}

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'order', 'product', 'quantity', 'price', 'total_cost']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_price_field(self):
        """
        Tests:
        field uses get_price_value method;
        """
        field = self.get_serializer_field(self.serializer, 'price')
        self.assertEqual(field.method_name, 'get_price_value')

    def test_get_price_value_returns_0_if_price_is_none(self):
        product = create_test_product()
        order_product = create_test_order_product(product=product)

        self.assertEqual(self.serializer.get_price_value(order_product), 0)

    def test_get_price_value_returns_correct_price(self):
        order_product = create_test_order_product(price=1000)

        self.assertEqual(self.serializer.get_price_value(order_product), order_product.price.value)


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
            'customer',
            'products',
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

    def test_customer_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'customer')
        self.assertTrue(field.read_only)

    def test_products_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'products')
        self.assertTrue(field.read_only)

    def test_updated_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'updated')
        self.assertTrue(field.read_only)

    def test_created_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'created')
        self.assertTrue(field.read_only)
