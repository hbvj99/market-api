from datetime import timedelta

from .base import *

SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = '*'

INSTALLED_APPS += [
    'drf_yasg'
]

INTERNAL_IPS = ['127.0.0.1', ]  # required for drf_yasg

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ['rest_framework.authentication.SessionAuthentication'] + \
                                                   REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Static
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# to make development easy
TIME_ZONE = 'UTC'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
FROM_MAIL = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_USE_TLS = True
TOKEN_TIMEOUT_DAYS = 2

if DEBUG is False:
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }

# SIMPLE JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
}

# Security (SSL)
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 63072000  # 2 years
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_REFERRER_POLICY = 'same-origin'
CSRF_COOKIE_SECURE = True

# Other secure headers
USE_X_FORWARDED_HOST = True
X_FRAME_OPTIONS = 'DENY'

# Token expiry in seconds
PASSWORD_RESET_TIMEOUT = 432000  # 4 days
