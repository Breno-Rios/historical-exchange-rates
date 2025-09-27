# config/settings/dev.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database (exemplo SQLite para dev)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Logging detalhado
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # Apenas logs essenciais do Django
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',  # mostra WARNING, ERROR e CRITICAL
            'propagate': True,
        },
        # Mostra requisições HTTP
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}