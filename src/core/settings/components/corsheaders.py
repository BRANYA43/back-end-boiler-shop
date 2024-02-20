from core.settings.components.base import INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS += ['corsheaders']
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
]
