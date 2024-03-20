from rest_framework.serializers import ModelSerializer

from orders import serializers
from orders.models import Order, Customer, OrderProduct
from utils.tests import CustomTestCase, creators


class CustomerCreateSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.CustomerCreateSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [ModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer_class, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['full_name', 'email', 'phone']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)

    def test_serializer_clean_phone(self):
        data = {
            'order': creators.create_test_order().uuid,
            'full_name': 'Rick Sanchez',
            'email': 'rick.sanchez@test.com',
        }
        phones = [
            '+380501234567',
            '0501234567',
            '+38 050 123 45 67',
            '050 123 45 67',
        ]
        expected_phone = '+38 (050) 123 45-67'

        for phone in phones:
            data.setdefault('phone', phone)
            serializer = self.serializer_class(data=data)

            self.assertTrue(serializer.is_valid())
            self.assertEqual(serializer.validated_data['phone'], expected_phone)


class OrderProductCreateSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.OrderProductCreateSerializer

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['product', 'quantity']
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


class OrderSetCreateSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.product = creators.create_test_product(price=1000)
        self.serializer_class = serializers.OrderSetCreateSerializer
        self.data = {
            'order': {},
            'customer': {
                'full_name': 'Rick Sanchez',
                'email': 'rick.sanchez@test.com',
                'phone': '+38(000) 000 00-00',
            },
            'products': [{'product': self.product.uuid}],
        }

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['order', 'customer', 'products']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)

    def test_serializer_creates_and_saves_order(self):
        self.assertEqual(Order.objects.count(), 0)

        serializer = self.serializer_class(data=self.data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()

        self.assertEqual(Order.objects.count(), 1)

    def test_serializer_creates_and_saves_customer(self):
        self.assertEqual(Customer.objects.count(), 0)

        serializer = self.serializer_class(data=self.data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()

        self.assertEqual(Customer.objects.count(), 1)

    def test_serializer_creates_and_saves_products(self):
        self.assertEqual(OrderProduct.objects.count(), 0)

        serializer = self.serializer_class(data=self.data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()

        self.assertEqual(OrderProduct.objects.count(), 1)
