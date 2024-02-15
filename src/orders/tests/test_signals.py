from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order_product, create_test_product


class SetOrderProductPriceSignalTest(CustomTestCase):
    def test_signal_sets_price_before_saving_order_product(self):
        product = create_test_product(price=1000)
        order_product = create_test_order_product(product=product)

        self.assertEqual(order_product.price.value, product.price)

    def test_signal_doesnt_set_price_before_saving_order_product_if_price_is_already_set(self):
        product_1 = create_test_product(price=1000)
        product_2 = create_test_product(price=2000)
        order_product = create_test_order_product(product=product_1)

        self.assertEqual(order_product.price.value, product_1.price)

        order_product.product = product_2
        order_product.save()

        self.assertEqual(order_product.price.value, product_1.price)
