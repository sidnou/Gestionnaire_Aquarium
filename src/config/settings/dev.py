from .base import *
import os

DEBUG = True
ALLOWED_HOSTS =[]

# Base de données SQLite pour dev rapide
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
