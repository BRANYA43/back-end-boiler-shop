from utils.mixins import UUIDMixin
from utils.tests import CustomTestCase


class UUIDMixinTest(CustomTestCase):
    def setUp(self) -> None:
        self.mixin = UUIDMixin

    def test_uuid_field(self):
        field = self.get_model_field(self.mixin, 'uuid')
        self.assertTrue(field.primary_key)
