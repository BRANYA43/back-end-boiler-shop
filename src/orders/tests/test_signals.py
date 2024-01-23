from orders.models import Customer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order


class CreateSpecificationOfProductSignalTest(CustomTestCase):
    def test_signal_creates_specification_after_saving_product(self):
        self.assertEqual(Customer.objects.count(), 0)

        order = create_test_order()

        self.assertEqual(Customer.objects.count(), 1)

        customer = Customer.objects.first()

        self.assertEqual(customer.uuid, order.customer.uuid)

    def test_signal_creates_specification_once(self):
        self.assertEqual(Customer.objects.count(), 0)

        product = create_test_order()

        self.assertEqual(Customer.objects.count(), 1)

        product.save()

        self.assertEqual(Customer.objects.count(), 1)
