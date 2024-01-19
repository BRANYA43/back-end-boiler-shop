from rest_framework.serializers import HyperlinkedModelSerializer

from utils.serializers import AttributeSerializer, ImageSerializer
from utils.tests import CustomTestCase


class ImageSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = ImageSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'name', 'image', 'updated', 'created']
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


class AttributeSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = AttributeSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'name', 'value']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)
