import re

from django.core.exceptions import ValidationError
import regex

PHONE_PATTERN = r'^\+?(38)?[\s\-]?\(?(?!38)(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{2})[\s\-]?(\d{2})$'
INVALID_PHONE_ERROR_MESSAGE = 'Invalid phone. Please enter correct phone by this pattern 380501234567 or 0501234567.'
INVALID_NAME_ERROR_MESSAGE = 'Invalid characters: {}. Please enter correct name.'


def validate_phone(value):
    if re.match(PHONE_PATTERN, value) is None:
        raise ValidationError(INVALID_PHONE_ERROR_MESSAGE, code='invalid_phone')


def validate_name(value):
    if symbols := regex.findall(r'[^\-\p{L}`\'\s]', value):
        raise ValidationError(INVALID_NAME_ERROR_MESSAGE.format(symbols), code='invalid_name')
