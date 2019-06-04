"""
Django settings for manti.by project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import raven


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ""

DEBUG = False

COMPRESS_ENABLED = True

TEMPLATE_DEBUG = False


# Application definition

INSTALLED_APPS = [
    "api",
    "blog",
    "core",
    "gallery",
    "profiles",
    "shortener",
    "taggit",
    "sorl.thumbnail",
    "compressor",
    "modeltranslation",
    "django_celery_results",
    "raven.contrib.django.raven_compat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
    "core.middleware.language.LocaleMiddleware",
    "core.middleware.response.ResponseMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.common.global_template_vars",
            ],
            "debug": False,
        },
    }
]

WSGI_APPLICATION = "core.wsgi.application"

BASE_URL = "https://manti.by"

SESSION_COOKIE_DOMAIN = ".manti.by"

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

# Cache backend
# https://docs.djangoproject.com/en/1.10/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "be"
ugettext = lambda s: s
LANGUAGES = (
    ("be", ugettext("Belarussian")),
    ("ru", ugettext("Russian")),
    ("en", ugettext("English")),
)

LOCALE_PATHS = (os.path.join(PROJECT_DIR, "locale"),)
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_URLS = {"be": "manti.by", "ru": "ru.manti.by", "en": "en.manti.by"}

DATE_FORMAT = "d E Y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(PROJECT_DIR, "content")
MEDIA_URL = "/content/"

FILE_UPLOAD_PERMISSIONS = 0o644

# Login redirect url

LOGIN_URL = "/profiles/login/"


# Sorl thumbnailer settings

THUMBNAIL_REDIS_HOST = "localhost"
THUMBNAIL_REDIS_PORT = "6379"
THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.redis_kvstore.KVStore"
THUMBNAIL_QUALITY = 85

# Email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 2525

DEFAULT_FROM_EMAIL = "admin@manti.by"
DEFAULT_TO_EMAIL = ""


# Allowed hosts

ALLOWED_HOSTS = ["127.0.0.1"]


# Static compressor settings

COMPRESS_OUTPUT_DIR = "cache"
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_CSS_HASHING_METHOD = None

# Celery settings

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "django-db"


# Meta tags info

META_TITLE = "Welcome to official blog of Alex Manti."
META_DESCRIPTION = "Official blog of Alex Manti. My music, photos and info about me."


# Instagram settings

INSTAGRAM_USER_ID = ""
INSTAGRAM_CLIENT_ID = ""
INSTAGRAM_ACCESS_TOKEN = ""
INSTAGRAM_CLIENT_SECRET = ""


# Sentry integration

ROOT_DIR = os.path.dirname((os.path.dirname(PROJECT_DIR)))
RAVEN_CONFIG = {"dsn": "", "release": raven.fetch_git_sha(ROOT_DIR)}
