from products.models import Category, Product, ProductImageSet, Specification, Stock
from utils.models import Attribute, Image
from utils.tests import CustomTestCase


class ProductImageSetModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = ProductImageSet

    def test_uuid_field(self):
        """
        Tests:
        uuid field is primary key;
        """
        field = self.get_model_field(self.model, 'uuid')
        self.assertTrue(field.primary_key)

    def test_images_field(self):
        """
        Tests:
        image field has relation many to many;
        image field has related model as Image;
        image field can be blank;
        """
        field = self.get_model_field(self.model, 'images')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Image)
        self.assertTrue(field.blank)

    def test_product_field(self):
        """
        Tests:
        product field has relation one ot one;
        product field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)


class SpecificationModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Specification

    def test_model_has_necessary_fields(self):
        necessary_field = ['uuid', 'product', 'attributes']
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_uuid_field(self):
        """
        Tests:
        uuid field is primary key;
        """
        field = self.get_model_field(self.model, 'uuid')
        self.assertTrue(field.primary_key)

    def test_product_field(self):
        """
        Tests:
        product field has relation one ot one;
        product field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)

    def test_attributes_field(self):
        """
        Tests:
        attributes field has relation many to many;
        attributes field has related_model as Attribute;
        """
        field = self.get_model_field(self.model, 'attributes')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Attribute)

    def test_model_is_created_after_creating_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

    def test_model_is_deleted_after_deleting_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        category = Category.objects.create(name='category')
        product = Product.objects.create(name='product', slug='slug', category=category, price=1000)

        self.assertEqual(Specification.objects.count(), 1)

        product.delete()

        self.assertEqual(Specification.objects.count(), 0)


class ProductModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Product

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

    def test_uuid_field(self):
        """
        Tests:
        uuid field is primary key;
        """
        field = self.get_model_field(self.model, 'uuid')
        self.assertTrue(field.primary_key)

    def test_name_field(self):
        """
        Tests:
        name field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertEqual(field.max_length, 50)

    def test_slug_field(self):
        """
        Tests:
        slug field has max length as 50;
        slug field is unique;
        """
        field = self.get_model_field(self.model, 'slug')
        self.assertEqual(field.max_length, 50)
        self.assertTrue(field.unique)

    def test_category_field(self):
        """
        Tests:
        category field has relation many to one;
        category field has Category as related model;
        """
        field = self.get_model_field(self.model, 'category')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Category)

    def test_stock_field(self):
        """
        Tests:
        stock field is Stock.IN_STOCK by default;
        stock field has Stock.choices;
        """
        field = self.get_model_field(self.model, 'stock')
        self.assertEqual(field.default, Stock.IN_STOCK)
        self.assertEqual(field.choices, Stock.choices)

    def test_price_field(self):
        """
        Tests:
        price field has max digits as ten;
        price field has decimal places as two;
        """
        field = self.get_model_field(self.model, 'price')
        self.assertEqual(field.max_digits, 10)
        self.assertEqual(field.decimal_places, 2)

    def test_is_displayed_field(self):
        """
        Tests:
        is_displayed field is true by default;
        """
        field = self.get_model_field(self.model, 'is_displayed')
        self.assertTrue(field.default)

    def test_description_field(self):
        """
        Tests:
        description field can be null;
        description field can be blank;
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


class CategoryModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Category

    def test_model_has_necessary_fields(self):
        necessary_fields = ['uuid', 'name', 'parent']
        self.assertModelHasNecessaryFields(self.model, necessary_fields)

    def test_uuid_field(self):
        """
        Requirements:
        uuid field is primary_key'
        """
        field = self.get_model_field(self.model, 'uuid')
        self.assertTrue(field.primary_key)

    def test_name_field(self):
        """
        Requirements:
        name field is unique;
        name field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertTrue(field.unique)
        self.assertEqual(field.max_length, 50)

    def test_parent_field(self):
        """
        Requirements:
        parent field has relation many to one;
        parent field has Category as related model;
        parent field can be null;
        parent field can be blank;
        parent field is None by default;
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

        self.assertIsNotNone(parent.sub_categories.first())
        self.assertTrue(parent.is_parent_category)

    def test_is_parent_category_property_is_false_if_sub_categories_are_none(self):
        parent = Category.objects.create(name='parent')

        self.assertIsNone(parent.sub_categories.first())
        self.assertFalse(parent.is_parent_category)
