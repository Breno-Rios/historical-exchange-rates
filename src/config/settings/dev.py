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
    "version": 1,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "DEBUG"},
}
