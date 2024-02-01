from orders.models import Customer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order, create_test_order_product, create_test_product


class SetOrderProductPriceSignalTest(CustomTestCase):
    def test_signal_sets_price_before_saving_order_product(self):
        product = create_test_product(price=1000)
        order_product = create_test_order_product(product=product)

        self.assertEqual(order_product.price.value, product.price.value)

    def test_signal_doesnt_set_price_before_saving_order_product_if_price_is_already_set(self):
        product_1 = create_test_product(price=1000)
        product_2 = create_test_product(price=2000)
        order_product = create_test_order_product(product=product_1)

        self.assertEqual(order_product.price.value, product_1.price.value)

        order_product.product = product_2
        order_product.save()

        self.assertEqual(order_product.price.value, product_1.price.value)


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
