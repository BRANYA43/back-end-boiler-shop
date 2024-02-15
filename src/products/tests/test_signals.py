from products.models import ProductImageSet, Specification
from utils.tests import CustomTestCase, creators
from utils.tests.creators import create_test_product


class SetProductPriceSignalTest(CustomTestCase):
    def test_signal_set_product_price_as_value_of_price_model(self):
        price = creators.create_test_price(value=1000)
        self.assertEqual(price.product.price, price.value)


class CreateSpecificationOfProductSignalTest(CustomTestCase):
    def test_signal_creates_specification_after_saving_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

    def test_signal_creates_specification_once(self):
        self.assertEqual(Specification.objects.count(), 0)

        product = create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

        product.save()

        self.assertEqual(Specification.objects.count(), 1)


class CreateProductImageSetSignalTest(CustomTestCase):
    def test_signal_creates_product_image_set_after_saving_product(self):
        self.assertEqual(ProductImageSet.objects.count(), 0)

        create_test_product()

        self.assertEqual(ProductImageSet.objects.count(), 1)

    def test_signal_creates_product_image_set_once(self):
        self.assertEqual(ProductImageSet.objects.count(), 0)

        product = create_test_product()

        self.assertEqual(ProductImageSet.objects.count(), 1)

        product.save()

        self.assertEqual(ProductImageSet.objects.count(), 1)
