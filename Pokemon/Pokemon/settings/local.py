from .base import *

SECRET_KEY = 'django-insecure-(e52!_ly!qb%0(9^i-8sgncb5f1-$8h-+o91et*)9!2q-xum6-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'Chileylau020',
        'NAME': 'Pokemon',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

STATIC_URL = '/static/'

