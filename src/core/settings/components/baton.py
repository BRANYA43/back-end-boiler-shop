from core.settings.components.base import INSTALLED_APPS

INSTALLED_APPS.insert(0, 'baton')
INSTALLED_APPS.append('baton.autodiscover')

BATON = {
    'SITE_HEADER': 'Boiler Shop',
    'SITE_TITLE': 'Boiler Shop',
    'INDEX_TITLE': 'Site Administration',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright © 2023 <a href="https://www.otto.to.it">Otto srl</a>',  # noqa
    'POWERED_BY': '<a href="https://www.otto.to.it">Otto srl</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'GRAVATAR_ENABLED': True,
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'FORCE_THEME': None,
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'MENU': (),
}
