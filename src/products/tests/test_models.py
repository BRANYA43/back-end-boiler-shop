from django.db.models import ProtectedError

from products.models import Category, Product, ProductImageSet, Specification, Stock, Price
from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Attribute
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product, create_test_price


class PriceModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Price

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_product_field(self):
        """
        Tests:
        field has relation many ot one;
        field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Product)

    def test_price_field(self):
        """
        Tests:
        field has max digits as 10;
        field has decimal places as 2;
        """
        field = self.get_model_field(self.model, 'price')
        self.assertEqual(field.max_digits, 10)
        self.assertEqual(field.decimal_places, 2)

    def test_created_field(self):
        """
        Tests:
        field sets date only when model is created;
        """
        field = self.get_model_field(self.model, 'created')
        self.assertTrue(field.auto_now_add)


class ProductImageSetModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = ProductImageSet

    def test_model_inherit_necessary_mixins(self):
        mixins = [ImageSetMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_product_field(self):
        """
        Tests:
        field has relation one ot one;
        field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)

    def test_model_is_created_after_creating_product(self):
        self.assertEqual(self.model.objects.count(), 0)

        create_test_product()

        self.assertEqual(self.model.objects.count(), 1)

    def test_model_is_deleted_after_deleting_product(self):
        self.assertEqual(self.model.objects.count(), 0)

        product = create_test_product()

        self.assertEqual(self.model.objects.count(), 1)

        product.delete()

        self.assertEqual(self.model.objects.count(), 0)


class SpecificationModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Specification

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_field = ['uuid', 'product', 'attributes']
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_product_field(self):
        """
        Tests:
        field has relation one ot one;
        field has related model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)

    def test_attributes_field(self):
        """
        Tests:
        field has relation many to many;
        field has related model as Attribute;
        """
        field = self.get_model_field(self.model, 'attributes')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Attribute)

    def test_model_is_created_after_creating_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

    def test_model_is_deleted_after_deleting_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        product = create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

        product.delete()

        self.assertEqual(Specification.objects.count(), 0)


class ProductModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Product

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin, CreatedAndUpdatedDateTimeMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_fields = [
            'uuid',
            'name',
            'slug',
            'category',
            'stock',
            'price',
            'description',
            'is_displayed',
            'updated',
            'created',
        ]
        self.assertModelHasNecessaryFields(self.model, necessary_fields)

    def test_name_field(self):
        """
        Tests:
        field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertEqual(field.max_length, 50)

    def test_slug_field(self):
        """
        Tests:
        field has max length as 50;
        field is unique;
        """
        field = self.get_model_field(self.model, 'slug')
        self.assertEqual(field.max_length, 50)
        self.assertTrue(field.unique)

    def test_category_field(self):
        """
        Tests:
        field has relation many to one;
        field has Category as related model;
        """
        field = self.get_model_field(self.model, 'category')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Category)

    def test_stock_field(self):
        """
        Tests:
        field is Stock.IN_STOCK by default;
        field has Stock.choices;
        """
        field = self.get_model_field(self.model, 'stock')
        self.assertEqual(field.default, Stock.IN_STOCK)
        self.assertEqual(field.choices, Stock.choices)

    def test_is_displayed_field(self):
        """
        Tests:
        field is true by default;
        """
        field = self.get_model_field(self.model, 'is_displayed')
        self.assertTrue(field.default)

    def test_description_field(self):
        """
        Tests:
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'description')
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_total_grade_property_returns_correct_grade_of_product(self):
        product = self.model()
        product.grade = {1: 5, 2: 10, 3: 10, 4: 20, 5: 40}
        grade = sum([g * c for g, c in product.grade.items()])
        count = sum(product.grade.values())
        expected_total_grade = round(grade / count, 2)

        self.assertEqual(product.total_grade, expected_total_grade)

    def test_price_property_returns_latest_created_price(self):
        product = create_test_product()
        price_1 = create_test_price(product, price=1000)

        self.assertEqual(price_1.price, product.price.price)

        price_2 = create_test_price(product, price=2000)

        self.assertNotEqual(price_1.price, product.price.price)
        self.assertEqual(price_2.price, product.price.price)

    def test_model_allows_category_to_be_deleted(self):
        product = create_test_product()
        category = product.category

        with self.assertRaises(ProtectedError):
            category.delete()


class CategoryModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Category

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_fields = ['uuid', 'name', 'parent']
        self.assertModelHasNecessaryFields(self.model, necessary_fields)

    def test_name_field(self):
        """
        Tests:
        field is unique;
        field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertTrue(field.unique)
        self.assertEqual(field.max_length, 50)

    def test_parent_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Category;
        field can be null;
        field can be blank;
        field is None by default;
        """
        field = self.get_model_field(self.model, 'parent')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, self.model)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)
        self.assertIsNone(field.default)

    def test_parent_field_is_set_as_null_if_parent_category_is_deleted(self):
        parent = Category.objects.create(name='parent')
        sub = Category.objects.create(name='sub', parent=parent)

        self.assertIsNotNone(sub.parent)

        parent.delete()
        sub.refresh_from_db()

        self.assertIsNone(sub.parent)

    def test_is_sub_category_property_is_true_if_parent_is_not_none(self):
        parent = Category.objects.create(name='parent')
        sub = Category.objects.create(name='sub', parent=parent)

        self.assertIsNotNone(sub.parent)
        self.assertTrue(sub.is_sub_category)

    def test_is_sub_category_property_is_false_if_parent_is_none(self):
        sub = Category.objects.create(name='sub')

        self.assertIsNone(sub.parent)
        self.assertFalse(sub.is_sub_category)

    def test_is_parent_category_property_is_true_if_sub_categories_are_not_none(self):
        parent = Category.objects.create(name='parent')
        sub = Category.objects.create(name='sub', parent=parent)  # noqa

        self.assertIsNotNone(parent.subs.first())
        self.assertTrue(parent.is_parent_category)

    def test_is_parent_category_property_is_false_if_sub_categories_are_none(self):
        parent = Category.objects.create(name='parent')

        self.assertIsNone(parent.subs.first())
        self.assertFalse(parent.is_parent_category)
