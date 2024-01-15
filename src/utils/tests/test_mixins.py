from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin
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
