# Django settings for lfc buildout.

import os
DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False
COMPRESS_CACHE_BACKEND = 'locmem:///'

ADMINS = (
    # ('name', 'email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                                 # Or path to database file if using sqlite3.
        'USER': '',                                 # Not used with sqlite3.
        'PASSWORD': '',                             # Not used with sqlite3.
        'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# static files settings
STATIC_URL = '/static/'
STATIC_ROOT = DIRNAME + "/sitestatic"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = DIRNAME + "/media"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    "pagination.middleware.PaginationMiddleware",
    "lfc.utils.middleware.LFCMiddleware",
    "lfc_developement_tools.middleware.AJAXSimpleExceptionResponse",
    "lfc_developement_tools.middleware.ProfileMiddleware",
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    "compressor",
    "lfc_theme",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    "django.contrib.flatpages",
    "django.contrib.sitemaps",
    "django.contrib.comments",
    "django_extensions",
    "lfc",
    "lfc_page",
    "lfc_blog",
    "lfc_bench",
    "lfc_contact_form",
    "lfc_compositor",
    "lfc_portlets",
    "portlets",
    "tagging",
    "pagination",
    "workflows",
    "permissions",
    "gunicorn",
    "lfc_rss_tags",
    # "debug_toolbar",
)

# For sql_queries
INTERNAL_IPS = (
    "127.0.0.1",
)

CACHE_MIDDLEWARE_KEY_PREFIX = "lfc"
CACHE_BACKEND = 'dummy:///'

FORCE_SCRIPT_NAME=""
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'lfc.context_processors.main',
)

DEFAULT_FROM_EMAIL = ""
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
         "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
         },
         "simple": {
            "format": "%(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
         },
    },
    "handlers": {
         "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/Users/Kai/Temp/lfc.log',
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

PAGINATION_DEFAULT_PAGINATION = 5
PAGINATION_DEFAULT_WINDOW = 1

LANGUAGES = (("en", u"English"), ("de", u"German",))
LFC_MULTILANGUAGE = len(LANGUAGES) > 1
LFC_MANAGE_WORKFLOWS =  True
LFC_MANAGE_PERMISSIONS =  True
LFC_MANAGE_APPLICATIONS = True
LFC_MANAGE_USERS = True

LFC_MANAGE_META_DATA = True
LFC_MANAGE_SEO =  True
LFC_MANAGE_COMMENTS = True
LFC_MANAGE_PORTLETS = True
LFC_MANAGE_IMAGES = True
LFC_MANAGE_FILES = True

LFC_TAGS = [
    "lfc_tags",
]

try:
    from local_settings import *
except ImportError:
    pass
