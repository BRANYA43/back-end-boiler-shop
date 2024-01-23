from orders.models import Order
from utils.mixins import UUIDMixin, CreatedAndUpdatedDateTimeMixin
from utils.tests import CustomTestCase


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
