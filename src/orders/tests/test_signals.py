from orders.models import Customer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order, create_test_order_product, create_test_price


class SetOrderProductPriceSignalTest(CustomTestCase):
    def test_signal_sets_price_before_saving_order_product(self):
        price = create_test_price()
        product = price.product
        order_product = create_test_order_product(product=product)

        self.assertEqual(order_product.price.price, product.price.price)

    def test_signal_doesnt_set_price_before_saving_order_product_if_price_is_already_set(self):
        price_1 = create_test_price(price=1000)
        price_2 = create_test_price(price=2000)
        product_1 = price_1.product
        product_2 = price_2.product
        order_product = create_test_order_product(product=product_1)

        self.assertEqual(order_product.price.price, product_1.price.price)

        order_product.product = product_2
        order_product.save()

        self.assertEqual(order_product.price.price, product_1.price.price)


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
