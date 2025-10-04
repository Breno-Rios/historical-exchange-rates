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
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} - {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',  # usa o formato detalhado
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # DEBUG para ainda mais detalhamento se quiser
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG',  # mostra detalhes das requisições HTTP
            'propagate': False,
        },
        # logger customizado para a sua app
        'myapp': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}