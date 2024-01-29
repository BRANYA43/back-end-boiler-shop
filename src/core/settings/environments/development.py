"""
Development setting file
"""
from core.settings.components import BASE_DIR
from core.settings.components.base import INSTALLED_APPS, MIDDLEWARE


def show_toolbar(request):
    return True


# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': show_toolbar,
# }

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
