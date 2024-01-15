from products.models import Category, Product, Specification
from utils.tests import CustomTestCase


class CreateSpecificationOfProductSignalTest(CustomTestCase):
    def test_specification_is_created_after_saving_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

    def test_specification_is_created_once_after_saving_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        product = Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

        product.save()

        self.assertEqual(Specification.objects.count(), 1)
