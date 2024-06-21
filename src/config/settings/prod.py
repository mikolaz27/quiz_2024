import os

from config.settings.base import *  # NOQA

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["ec2-54-196-153-15.compute-1.amazonaws.com", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_ROOT = BASE_DIR / "static/"  # NOQA
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "media/"  # NOQA
MEDIA_URL = "media/"
