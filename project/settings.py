import os
import logging.config

import dj_database_url


ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'project.urls'
SESSION_COOKIE_AGE = 2 * 60 * 60  # 2 hours, in seconds
WSGI_APPLICATION = 'project.wsgi.application'


# Environments settings
DEBUG = os.getenv('DEBUG') == 'true'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
FRONTEND_BASE_URL = os.getenv('FRONTEND_BASE_URL')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # disable Django’s static file handling
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Django libraries and apps below here
    'application',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'drf_yasg',
    'rest_framework',

    # Wagtail apps
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    # Wagtail related apps
    'modelcluster',
    'taggit',
]


# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # CorsMiddleware should be placed as high as possible and above WhiteNoiseMiddleware in particular
    'corsheaders.middleware.CorsMiddleware',
    # WhiteNoise middleware should be above all and just below SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',


    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Wagtail middlewares
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DATABASES = dict()
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=300)


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Swagger settings
SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'list',
    'OPERATIONS_SORTER': 'method',
    'REFETCH_SCHEMA_ON_LOGOUT': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'USE_SESSION_AUTH': True,
}
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'


# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-files')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media-files')

# CORS settings
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',  # local development environment of frontend application
)

# Media files storage configs
DEFAULT_FILE_STORAGE = os.getenv("DEFAULT_FILE_STORAGE")

if DEFAULT_FILE_STORAGE == "storages.backends.gcloud.GoogleCloudStorage":
    GS_BUCKET_NAME = os.getenv("STAGING_GCS_BUCKET_NAME")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("STAGING_GCS_BUCKET_CREDENTIALS")
    GS_DEFAULT_ACL = 'publicRead'
    GS_FILE_OVERWRITE = False

elif DEFAULT_FILE_STORAGE == "storages.backends.azure_storage.AzureStorage":
    AZURE_ACCOUNT_NAME = os.getenv("AZURE_BUCKET_ACCOUNT_NAME")
    AZURE_ACCOUNT_KEY = os.getenv("AZURE_BUCKET_CREDENTIALS")
    AZURE_CONTAINER = os.getenv("AZURE_BUCKET_NAME")

# Wagtail settings
WAGTAIL_SITE_NAME = 'City of Helsinki'
WAGTAIL_ENABLE_UPDATE_CHECK = False
WAGTAILIMAGES_IMAGE_MODEL = 'application.CustomImage'
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 700 * 1024  # i.e. 700 KB
WAGTAILIMAGES_MAX_IMAGE_PIXELS = 2000000  # 2 million pixels


# Logging
def skip_static_requests(record):
    static_request = record.args[0].startswith('GET /static/')
    return not static_request


logging_configurations = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'skip_static_requests': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_static_requests
        }
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': [],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'filters': ['skip_static_requests'],
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
LOGGING_CONFIG = None
logging.config.dictConfig(logging_configurations)
