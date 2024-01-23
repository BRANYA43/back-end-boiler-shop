from django.core.exceptions import ValidationError

from orders.validators import validate_phone
from utils.tests import CustomTestCase


class ValidatePhoneTest(CustomTestCase):
    def test_validator_doesnt_raise_error(self):
        value = '+38 (000) 000 00-00'
        validate_phone(value)  # not raise

    def test_validator_raise_error(self):
        invalid_values = [
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38-050-123-45-67',
            '050-123-45-67',
            '38 (050) 123 45 67',
            '38-050-123 45 67',
            '050 123 45 67',
            '+38050-123-45-67',
            '+38(050)123-45-67',
            '38-050-123-45-67',
            '050-123-45-67',
            '38 (050) 123-4567',
            '+38 050 123-4567',
            '050 123-4567',
            '+38050 123-4567',
            '38 (050) 1234567',
            '+38-050-1234567',
            '050-1234567',
            '380501234567',
            '38(050)1234567',
        ]

        with self.assertRaises(ValidationError):
            for value in invalid_values:
                validate_phone(value)
