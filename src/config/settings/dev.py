import os

from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-#dlv8***nlb#xf3u32a$psx#_at(@j@9(yoaonefyq7%-gw*w$"

DEBUG = True

ALLOWED_HOSTS = []  # NOQA

INSTALLED_APPS += ["django_extensions"]  # NOQA

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
    "default_sql": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_URL = "static/"
