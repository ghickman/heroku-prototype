from default_settings import *


DEBUG = True
SERVE_MEDIA = DEBUG
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

DEVELOPMENT_SITE = True

#DEBUG_PROPAGATE_EXCEPTIONS = False

AWS_ACCESS_KEY_ID = 'AKIAJPTGK3KJ3JN3PJOA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'incuna-prototype'
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

