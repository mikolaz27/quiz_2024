import os

import mongoengine

from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-#dlv8***nlb#xf3u32a$psx#_at(@j@9(yoaonefyq7%-gw*w$"

DEBUG = True
ALLOWED_HOSTS = []  # NOQA

INSTALLED_APPS += ["django_extensions"]  # NOQA

mongoengine.connect(
    host=os.environ.get("DJANGO_MONGO_CONNECTION"),
)

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        },
    }
else:
    DATABASES = {
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": "quiz_db",
        #     "USER": "quiz_user",
        #     "PASSWORD": "admin",
        #     "HOST": "localhost",
        #     "PORT": "5432",
        # },
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
        # "default": {
        #     "ENGINE": "django.db.backends.sqlite3",
        #     "NAME": BASE_DIR / "db.sqlite3",  # NOQA
        # }
    }

STATIC_URL = "static/"
