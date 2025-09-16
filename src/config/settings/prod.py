# config/settings/prod.py
from .base import *

import os
from dotenv import load_dotenv

load_dotenv()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='*').split(',')

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {"level": "INFO", "class": "logging.FileHandler", "filename": "/var/log/django.log"},
    },
    "root": {"handlers": ["file"], "level": "INFO"},
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
