from products.models import Category
from utils.tests import CustomTestCase


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
