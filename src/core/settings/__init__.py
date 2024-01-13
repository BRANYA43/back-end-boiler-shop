"""
Combining settings for django project 
"""
from split_settings.tools import include, optional

from core.settings.components import env

_settings = (
    'components/base.py',
    'components/rest_framework.py',
    'components/baton.py',  # It must be last component
    'environments/{}.py'.format(env['DJANGO_SETTINGS_ENV'].lower()),
    optional('environments/local.py'),
)

include(*_settings)
