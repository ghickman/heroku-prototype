import os

from default_settings import *


# static
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
    }
}

# geodjango binaries
GDAL_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgdal.so'
GEOS_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgeos_c.so'

# wkhtmltopdf binary
WKHTMLTOPDF_CMD = '/app/.heroku/wkhtmltopdf'

