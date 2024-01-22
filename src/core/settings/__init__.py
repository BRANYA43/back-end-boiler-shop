"""
Combining settings for django project 
"""
from split_settings.tools import include, optional

from core.settings.components import env

_settings = (
    'components/base.py',
    'components/rest_framework.py',
    'components/baton.py',  # It must be last component
    'environments/{}.py'.format(env.get('DJANGO_SETTINGS_ENV', 'production').lower()),
    optional('environments/local.py'),
)

include(*_settings)
