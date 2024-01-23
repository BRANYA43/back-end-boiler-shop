import re

from django.core.exceptions import ValidationError

INVALID_PHONE_ERROR_MESSAGE = 'Invalid phone. Phone must be by pattern +38 (000) 000 00-00 .'


def validate_phone(value):
    pattern = r'^\+\d{2} \(\d{3}\) \d{3} \d{2}-\d{2}$'
    if re.match(pattern, value) is None:
        raise ValidationError(INVALID_PHONE_ERROR_MESSAGE, code='invalid_phone')
