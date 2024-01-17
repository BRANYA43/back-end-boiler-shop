from products.models import Category, Product, ProductImageSet, Specification
from utils.tests import CustomTestCase


class CreateSpecificationOfProductSignalTest(CustomTestCase):
    def test_signal_creates_specification_after_saving_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

    def test_signal_creates_specification_once(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        product = Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

        product.save()

        self.assertEqual(Specification.objects.count(), 1)


class CreateProductImageSetSignalTest(CustomTestCase):
    def test_signal_creates_product_image_set_after_saving_product(self):
        self.assertEqual(ProductImageSet.objects.count(), 0)

        category = Category.objects.create(name='category')
        Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(ProductImageSet.objects.count(), 1)

    def test_signal_creates_product_image_set_once(self):
        self.assertEqual(ProductImageSet.objects.count(), 0)

        category = Category.objects.create(name='category')
        product = Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(ProductImageSet.objects.count(), 1)

        product.save()

        self.assertEqual(ProductImageSet.objects.count(), 1)
