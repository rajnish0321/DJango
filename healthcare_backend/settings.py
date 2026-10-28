import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

BASE_DIR = Path(**file**).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY", "development-only-key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"rest_framework",
"rest_framework_simplejwt",
"healthcare",
]

DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql",
"NAME": os.getenv("DB_NAME"),
"USER": os.getenv("DB_USER"),
"PASSWORD": os.getenv("DB_PASSWORD"),
"HOST": os.getenv("DB_HOST", "localhost"),
"PORT": os.getenv("DB_PORT", "5432"),
}
}

REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES": [
"rest_framework_simplejwt.authentication.JWTAuthentication",
],
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.IsAuthenticated",
],
}

SIMPLE_JWT = {
"ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
"REFRESH_TOKEN_LIFETIME": timedelta(days=1),
"AUTH_HEADER_TYPES": ("Bearer",),
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
