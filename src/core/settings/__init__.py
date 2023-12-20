"""
Combining settings for django project 
"""

from os import environ as env

from split_settings.tools import include, optional

env.setdefault('DJANGO_ENV', 'development')

_settings = (
    'components/base.py',
    'environments/{}.py'.format(env['DJANGO_ENV']),
    optional('environments/local.py'),
)

include(*_settings)
