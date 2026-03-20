from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-503+j1il(u-)mktxz2oouw3%_odj@dbkzi(-(v%+mfk0upp!n$'

DEBUG = True
ALLOWED_HOSTS =[]

INSTALLED_APPS += ["django_browser_reload"]

MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
# Base de données SQLite pour dev rapide
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
