import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('George Hickman', 'george@ghickman.co.uk'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

# S3 Backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = 'client_media'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    # 'feincms.context_processors.add_page_if_missing', # This context processor frequently causes transaction aborted errors!
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'prototype.middleware.LoginRequiredMiddleware',
)

SECRET_KEY = 'w6s(#ase(&amp;$8qm@%e3xpnsy6ffw1vvg6j^d(^x1n0@wyx51hqh'

ROOT_URLCONF = 'prototype.urls'

WSGI_APPLICATION = 'prototype.wsgi.application'

INSTALLED_APPS = (
    # third party apps
    # 'feincms',
    # 'feincms.module.page',
    # 'feincms.module.medialibrary',
    'wkhtmltopdf',

    # third party util apps
    'gunicorn',
    'raven.contrib.django',
    'storages',

    # django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SENTRY_DSN = 'http://1d8d5aea88a74268bba0332eb74bbd1b:9f8e593ca03f4070836522083f14c4bc@sentry.incuna.com/4'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'procurement',
    }
}

try:
    from local_settings import *
except ImportError:
    pass

