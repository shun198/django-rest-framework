"""
Django settings for study project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECRET_KEYを.envから取得
SECRET_KEY = os.environ.get("SECRET_KEY")

# DEBUGを.envから取得
DEBUG = os.environ.get("DEBUG")

# ALLOWED_HOSTSを.envから取得
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "django_extensions",
    "relationships.apps.RelationshipsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "study.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "study.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# MySQLのパラメータを.envから取得
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # コンテナ内の環境変数をDATABASESのパラメータに反映
        "NAME": os.environ.get("MYSQL_DATABASE"),
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD"),
        "HOST": "db",
        "PORT": 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# 言語を日本語に設定
LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE")
# タイムゾーンをAsia/Tokyoに設定
TIME_ZONE = os.environ.get("TIME_ZONE")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOTを設定
# Djangoの管理者画面にHTML、CSS、Javascriptが適用されます
STATIC_ROOT = "/static/"
STATIC_URL = "/static/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "プロジェクト名",
    "DESCRIPTION": "詳細",
    "VERSION": "1.0.0",
    # オプション
    'SERVE_INCLUDE_SCHEMA': False,
}
