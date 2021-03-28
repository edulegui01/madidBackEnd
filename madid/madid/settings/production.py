from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'edulegui',
        'USER': 'edulegui',
        'PASSWORD':'lamasita123',
        'HOST':'localhost',
        'PORT': 5432
    }
}

STATIC_URL = '/static/'
