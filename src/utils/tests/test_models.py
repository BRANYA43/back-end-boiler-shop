from utils.models import Attribute, Image
from utils.tests import CustomTestCase
from utils.utils import get_upload_filename


class ImageModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Image

    def test_model_has_necessary_fields(self):
        necessary_fields = ['uuid', 'name', 'image', 'updated', 'created']
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
        name field is unique;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertEqual(field.max_length, 50)
        self.assertTrue(field.unique)

    def test_image_field(self):
        """
        Test:
        image field has upload to as get_upload_filename
        """
        field = self.get_model_field(self.model, 'image')
        self.assertIs(field.upload_to, get_upload_filename)


class AttributeModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Attribute

    def test_model_has_necessary_fields(self):
        necessary_fields = ['uuid', 'name', 'value']
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

    def test_value_field(self):
        """
        Tests:
        value field has max length as 50;
        """
        field = self.get_model_field(self.model, 'value')
        self.assertEqual(field.max_length, 50)
