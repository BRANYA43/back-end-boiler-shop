from django.core.exceptions import ValidationError

from orders.validators import validate_phone
from utils.tests import CustomTestCase


class ValidatePhoneTest(CustomTestCase):
    def test_validator_doesnt_raise_error(self):
        valid_phones = [
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '380501234567',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380671234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380991234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
        ]
        for phone in valid_phones:
            validate_phone(phone)  # not raise

    def test_validator_raise_error(self):
        invalid_phones = [
            '123456789',  # less than 12 digits
            'abc123456789',  # contains letters
            '+3805012345678',  # more than 12 digits
            '+38-(050)123-45-67)',  # extra closing parenthesis
            '+38050123a567',  # letters in the middle
        ]
        for phone in invalid_phones:
            with self.assertRaises(ValidationError):
                validate_phone(phone)
