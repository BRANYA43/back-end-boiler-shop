from django.db.models import PositiveIntegerField, ProtectedError

from orders.models import Order, Customer, OrderProduct
from products.models import Product, Price
from utils.mixins import UUIDMixin, CreatedAndUpdatedDateTimeMixin
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order, create_test_order_product, create_test_price


class OrderProductModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = OrderProduct

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_field = ['uuid', 'order', 'product', 'quantity', 'price']
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_order_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Order;
        """
        field = self.get_model_field(self.model, 'order')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Order)

    def test_product_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Product)

    def test_quantity_field(self):
        """
        Tests:
        field has 1 by default;
        field is only positive integer;
        """
        field = self.get_model_field(self.model, 'quantity')
        self.assertEqual(field.default, 1)
        self.assertIsInstance(field, PositiveIntegerField)

    def test_price_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Price;
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'price')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Price)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_price_field_is_set_before_saving_model_from_price_property_of_product(self):
        price = create_test_price()
        product = price.product
        order_product = create_test_order_product(product=product)

        self.assertEqual(order_product.price.value, product.price.value)

    def test_model_is_deleted_after_deleting_order(self):
        self.assertEqual(OrderProduct.objects.count(), 0)

        order_product = create_test_order_product()

        self.assertEqual(OrderProduct.objects.count(), 1)

        order_product.order.delete()

        self.assertEqual(OrderProduct.objects.count(), 0)

    def test_model_is_protected_for_deleting_product(self):
        self.assertEqual(OrderProduct.objects.count(), 0)

        order_product = create_test_order_product()

        self.assertEqual(OrderProduct.objects.count(), 1)

        with self.assertRaises(ProtectedError):
            order_product.product.delete()

    def test_model_is_protected_for_deleting_price(self):
        self.assertEqual(OrderProduct.objects.count(), 0)

        price = create_test_price()
        order_product = create_test_order_product(product=price.product)

        self.assertEqual(OrderProduct.objects.count(), 1)

        with self.assertRaises(ProtectedError):
            order_product.price.delete()

    def test_total_cost_property_returns_correct_value(self):
        price = create_test_price(value=500)
        order_product = create_test_order_product(product=price.product, quantity=20)
        expected_total_cost = order_product.price.value * order_product.quantity

        self.assertEqual(order_product.total_cost, expected_total_cost)


class CustomerModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Customer

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_field = ['uuid', 'order', 'full_name', 'email', 'phone']
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_order_field(self):
        """
        Tests:
        field has relation one to one;
        field has related model as Order;
        """
        field = self.get_model_field(self.model, 'order')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Order)

    def test_full_name_field(self):
        """
        Tests:
        field has max length as 100;
        field can be null;
        """
        field = self.get_model_field(self.model, 'full_name')
        self.assertEqual(field.max_length, 100)
        self.assertTrue(field.null)

    def test_email_field(self):
        """
        Tests:
        field can be null;
        """
        field = self.get_model_field(self.model, 'email')
        self.assertTrue(field.null)

    def test_phone_field(self):
        """
        Tests:
        field can be null;
        """
        field = self.get_model_field(self.model, 'phone')
        self.assertTrue(field.null)

    def test_model_is_created_after_creating_order(self):
        self.assertEqual(Customer.objects.count(), 0)

        order = create_test_order()

        self.assertEqual(Customer.objects.count(), 1)

        customer = Customer.objects.first()

        self.assertEqual(customer.uuid, order.customer.uuid)

    def test_model_is_deleted_after_deleting_order(self):
        order = create_test_order()

        self.assertEqual(Customer.objects.count(), 1)

        order.delete()

        self.assertEqual(Customer.objects.count(), 0)


class OrderModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Order

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin, CreatedAndUpdatedDateTimeMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_field = [
            'uuid',
            'delivery',
            'delivery_address',
            'payment',
            'is_paid',
            'status',
            'comment',
            'created',
            'updated',
        ]
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_delivery_field(self):
        """
        Tests:
        field has choices as Delivery.choices;
        field has Delivery.PICKUP by default
        """
        field = self.get_model_field(self.model, 'delivery')
        self.assertEqual(field.choices, self.model.Delivery.choices)
        self.assertEqual(field.default, self.model.Delivery.PICKUP)

    def test_delivery_address(self):
        """
        Tests:
        field has max length as 255;
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'delivery_address')
        self.assertEqual(field.max_length, 255)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_payment_field(self):
        """
        Tests:
        field has choices as Payment.choices;
        field has Payment.CASH_ON_DELIVERY by default;
        """
        field = self.get_model_field(self.model, 'payment')
        self.assertEqual(field.choices, self.model.Payment.choices)
        self.assertEqual(field.default, self.model.Payment.CASH_ON_DELIVERY)

    def test_is_paid_field(self):
        """
        Tests:
        field has False by default;
        """
        field = self.get_model_field(self.model, 'is_paid')
        self.assertFalse(field.default)

    def test_status_field(self):
        """
        Tests:
        field has choices as Status.choices;
        field has Status.IN_PROCESSING by default;
        """
        field = self.get_model_field(self.model, 'status')
        self.assertEqual(field.choices, self.model.Status.choices)
        self.assertEqual(field.default, self.model.Status.IN_PROCESSING)

    def tests_comment_field(self):
        """
        Tests:
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'comment')
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_total_cost_property_returns_correct_value(self):
        order = create_test_order()
        price_1 = create_test_price(value=1000)
        price_2 = create_test_price(value=2000)
        order_product_1 = create_test_order_product(order=order, product=price_1.product, quantity=3)
        order_product_2 = create_test_order_product(order=order, product=price_2.product, quantity=7)
        expected_total_cost = order_product_1.total_cost + order_product_2.total_cost
        order.refresh_from_db()

        self.assertEqual(order.total_cost, expected_total_cost)

    def test_total_cost_property_returns_0_if_order_products_are_empty(self):
        order = create_test_order()
        self.assertEqual(order.total_cost, 0)
