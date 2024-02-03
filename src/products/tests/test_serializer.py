from unittest.mock import MagicMock

from products.serializers import (
    CategorySerializer,
    ProductImageSetSerializer,
    ProductSerializer,
    SpecificationSerializer,
)
from utils.serializers import ReadOnlyHyperlinkedModelSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product, create_test_attribute, create_test_image


class ProductImageSetSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = ProductImageSetSerializer
        self.context = {'request': MagicMock()}

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [ReadOnlyHyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'product', 'images']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_serializer_returns_images_as_url_list_from_data(self):
        images = [create_test_image() for i in range(10)]
        image_set = create_test_product().image_set
        image_set.images.set(images)
        serializer = self.serializer(instance=image_set, context=self.context)
        expected_image_set = [image.image.url for image in image_set.images.all()]

        self.assertListEqual(serializer.data['images'], expected_image_set)


class SpecificationSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = SpecificationSerializer
        self.attributes = [create_test_attribute() for i in range(10)]

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [ReadOnlyHyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'product', 'all_attributes', 'card_attributes', 'detail_attributes']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_all_attributes_field(self):
        """
        Tests:
        field uses get_all_attribute_items method;
        """
        field = self.get_serializer_field(self.serializer, 'all_attributes')
        self.assertEqual(field.method_name, 'get_all_attribute_items')

    def test_card_attributes_field(self):
        """
        Tests:
        field uses get_card_attribute_names method;
        """
        field = self.get_serializer_field(self.serializer, 'card_attributes')
        self.assertEqual(field.method_name, 'get_card_attribute_names')

    def test_detail_attributes_field(self):
        """
        Tests:
        field uses get_detail_attribute_names method;
        """
        field = self.get_serializer_field(self.serializer, 'detail_attributes')
        self.assertEqual(field.method_name, 'get_detail_attribute_names')

    def test_get_all_attribute_items_method_returns_correct_dict(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)

        expected_dict = {attribute.name: attribute.value for attribute in self.attributes}

        self.assertDictEqual(self.serializer.get_all_attribute_items(specification), expected_dict)

    def test_get_card_attribute_names_method_returns_correct_names(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.card_attributes.set(self.attributes[:3])

        expected_names = [attribute.name for attribute in self.attributes[:3]]
        names = self.serializer.get_card_attribute_names(specification)
        names.sort()
        expected_names.sort()

        self.assertListEqual(names, expected_names)

    def test_get_detail_attribute_names_method_returns_correct_names(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.detail_attributes.set(self.attributes[:5])

        expected_names = [attribute.name for attribute in self.attributes[:5]]
        names = self.serializer.get_detail_attribute_names(specification)
        names.sort()
        expected_names.sort()

        self.assertListEqual(names, expected_names)


class ProductSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = ProductSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [ReadOnlyHyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = [
            'url',
            'uuid',
            'category',
            'name',
            'slug',
            'price',
            'price_value',
            'stock',
            'description',
            'specification',
            'image_set',
            'is_displayed',
            'updated',
            'created',
        ]
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_price_value_field(self):
        """
        Tests:
        field uses get_price_value method;
        """
        field = self.get_serializer_field(self.serializer, 'price_value')
        self.assertEqual(field.method_name, 'get_price_value')

    def test_get_price_value_returns_0_if_price_is_none(self):
        product = create_test_product()

        self.assertEqual(self.serializer.get_price_value(product), 0)

    def test_get_price_value_returns_correct_price(self):
        product = create_test_product(price=1000)

        self.assertEqual(self.serializer.get_price_value(product), product.price.value)


class CategorySerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = CategorySerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [ReadOnlyHyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'name', 'parent', 'subs']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)
