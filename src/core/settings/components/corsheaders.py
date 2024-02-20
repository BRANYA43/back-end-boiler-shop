from core.settings.components.base import INSTALLED_APPS, MIDDLEWARE
from core.settings import env

INSTALLED_APPS += ['corsheaders']
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = env.get('CORS_ALLOWED_ORIGINS', '').split()
