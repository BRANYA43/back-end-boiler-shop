from _decimal import Decimal
from unittest.mock import MagicMock

from rest_framework.serializers import HyperlinkedModelSerializer

from products.serializers import (
    CategorySerializer,
    ProductImageSetSerializer,
    ProductSerializer,
    SpecificationSerializer,
)
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_price, create_test_product, create_test_attribute, create_test_image


class ProductImageSetSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = ProductImageSetSerializer
        self.context = {'request': MagicMock()}

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'product', 'images']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

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
        self.context = {'request': MagicMock()}

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'product', 'all_attributes', 'card_attributes', 'detail_attributes']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_serializer_returns_all_attributes_as_dict_from_data(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)
        expected_all_attributes = {attribute.name: attribute.value for attribute in specification.all_attributes.all()}
        serializer = self.serializer(instance=specification, context=self.context)

        self.assertDictEqual(serializer.data['all_attributes'], expected_all_attributes)

    def test_serializer_returns_card_attributes_as_name_list_from_data(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.card_attributes.set(self.attributes[:3])
        expected_card_attributes = [attribute.name for attribute in specification.card_attributes.all()]
        serializer = self.serializer(instance=specification, context=self.context)

        self.assertListEqual(serializer.data['card_attributes'], expected_card_attributes)

    def test_serializer_returns_detail_attributes_as_name_list_from_data(self):
        specification = create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.detail_attributes.set(self.attributes[:5])
        expected_detail_attributes = [attribute.name for attribute in specification.detail_attributes.all()]
        serializer = self.serializer(instance=specification, context=self.context)

        self.assertListEqual(serializer.data['detail_attributes'], expected_detail_attributes)


class ProductSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = ProductSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
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
            'stock',
            'description',
            'is_displayed',
            'specification',
            'image_set',
            'updated',
            'created',
        ]
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_updated_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'updated')
        self.assertTrue(field.read_only)

    def test_created_field_is_read_only(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'created')
        self.assertTrue(field.read_only)

    def test_serializer_returns_correct_price_in_data(self):
        product = create_test_price(value=2000).product
        context = {'request': MagicMock()}

        serializer = self.serializer(instance=product, context=context)
        self.assertEqual(serializer.data['price'], Decimal(2000))


class CategorySerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = CategorySerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'name', 'parent', 'subs']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)
