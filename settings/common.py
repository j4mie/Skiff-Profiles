import os
import sys
from django.conf import global_settings
from . import secrets

PROJECT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], os.pardir))

# Add the apps directory to the PYTHONPATH
sys.path.append(os.path.join(PROJECT_PATH, 'apps'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DOMAIN = 'example.com'

ADMINS = (
    ('Thomas Parslow', 'tom@almostobsolete.net'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-GB'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

LOGIN_REDIRECT_URL = '/manage/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('media', os.path.join(PROJECT_PATH, 'media')),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'staticfiles', 'media')
MEDIA_URL = '/static/media/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

SECRET_KEY = secrets.SECRET_KEY

# Default to dummy cache, can be overridden in deployment-specific settings files
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    #    'django.middleware.cache.UpdateCacheMiddleware',
        'core.middleware.CompanyMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    #    'django.middleware.cache.FetchFromCacheMiddleware',
    )

    ROOT_URLCONF = 'urls'

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_PATH, 'templates'),
    )

    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'django.core.context_processors.static',
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.admin',
        'django.contrib.staticfiles',
        'south',
        'bootstrap',
    )