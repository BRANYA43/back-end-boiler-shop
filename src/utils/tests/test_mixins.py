from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Image
from utils.tests import CustomTestCase


class UUIDMixinTest(CustomTestCase):
    def setUp(self) -> None:
        self.mixin = UUIDMixin

    def test_uuid_field(self):
        field = self.get_model_field(self.mixin, 'uuid')
        self.assertTrue(field.primary_key)


class CreatedAndUpdatedDateTimeMixinTest(CustomTestCase):
    def setUp(self) -> None:
        self.mixin = CreatedAndUpdatedDateTimeMixin

    def test_created_field(self):
        field = self.get_model_field(self.mixin, 'created')
        self.assertTrue(field.auto_now_add)

    def test_updated_field(self):
        field = self.get_model_field(self.mixin, 'updated')
        self.assertTrue(field.auto_now)


class ImageSetMixinTest(CustomTestCase):
    def setUp(self) -> None:
        self.mixin = ImageSetMixin

    def test_uuid_field(self):
        """
        Tests:
        uuid field is primary key;
        """
        field = self.get_model_field(self.mixin, 'uuid')
        self.assertTrue(field.primary_key)

    def test_images_field(self):
        """
        Tests:
        image field has relation many to many;
        image field has related model as Image;
        image field can be blank;
        """
        field = self.get_model_field(self.mixin, 'images')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Image)
        self.assertTrue(field.blank)
