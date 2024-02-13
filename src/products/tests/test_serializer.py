from rest_framework.serializers import ModelSerializer

from products import serializers
from products.models import Category
from utils.tests import CustomTestCase, creators


class ProductSerializerMixinTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = type('ProductSerializer', (serializers.ProductSerializerMixin,), {})

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_price_field_returns_correct_price_value(self):
        product = creators.create_test_product(price=1000)
        data = self.serializer_class(product).data

        self.assertEqual(data['price'], product.price.value)

    def test_price_field_returns_0_if_price_is_none(self):
        product = creators.create_test_product()
        data = self.serializer_class(product).data

        self.assertEqual(data['price'], 0)

    def test_images_field_returns_correct_image_urls(self):
        image = creators.create_test_image()
        product = creators.create_test_product()
        product.image_set.images.set([image])
        data = self.serializer_class(product).data

        self.assertEqual(data['images'], [image.image.url])


class CategoryListSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.CategoryListSerializer

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['uuid', 'name', 'image', 'parent', 'children']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)

    def test_children_categories_are_returned_recurse(self):
        parent = creators.create_test_category()
        child = creators.create_test_category(parent=parent)
        all_data = self.serializer_class(Category.objects.all(), many=True).data[0]
        children_data = all_data['children'][0]

        self.assertEqual(children_data['uuid'], str(child.uuid))

    def test_children_categories_arent_duplicated_in_category_list(self):
        parent = creators.create_test_category()
        child = creators.create_test_category(parent=parent)
        data = self.serializer_class(Category.objects.all(), many=True).data[0]

        self.assertNotIn(child.uuid, data.values())


class CategoryDetailSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer_class = serializers.CategoryDetailSerializer

    def test_serializer_inherit_necessary_classes(self):
        classes = [ModelSerializer]
        for class_ in classes:
            self.assertTrue(self.serializer_class, class_)

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['uuid', 'name', 'image', 'parent', 'children', 'products']
        self.assertSerializerHasOnlyExpectedFields(self.serializer_class, expected_fields)

    def test_children_categories_are_returned_with_only_uuid_and_name_fields(self):
        parent = creators.create_test_category()
        child = creators.create_test_category(parent=parent)
        data = self.serializer_class(parent).data
        child_data = data['children'][0]

        self.assertEqual(len(child_data), 2)
        self.assertEqual(child_data['name'], child.name)
        self.assertEqual(child_data['uuid'], child.uuid)

    def test_foo(self):
        product = creators.create_test_product()
        data = self.serializer_class(product.category).data
        product_data = data['products'][0]

        self.assertEqual(len(product_data), 2)
        self.assertEqual(product_data['name'], product.name)
        self.assertEqual(product_data['uuid'], product.uuid)
