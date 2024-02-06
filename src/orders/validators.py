import re

from django.core.exceptions import ValidationError
import regex

PHONE_PATTERN = r'^\+?(38)?[\s\-]?\(?(?!38)(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{2})[\s\-]?(\d{2})$'


def validate_phone(value):
    message = 'Invalid phone. Please enter correct phone by this pattern 380501234567 or 0501234567.'
    code = 'invalid_phone'
    if re.match(PHONE_PATTERN, value) is None:
        raise ValidationError(message, code)


def validate_name(value):
    message = 'Invalid characters: {characters}. Please enter correct name.'
    code = 'invalid_full_name'
    if characters := regex.findall(r'[^\-\p{L}`\'\s]', value):
        raise ValidationError(message, code, params={'characters': characters})
