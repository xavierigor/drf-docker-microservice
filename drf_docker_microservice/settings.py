from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '9ixzz99$1i#@bbrex&m5fp@m5eyyry!m+4*lf@_475=d&u&7-&'

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'rest_framework',
    # ...
]

ROOT_URLCONF = 'drf_docker_microservice.urls'


WSGI_APPLICATION = 'drf_docker_microservice.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "db",
        'PORT': "5432",
    }
}


TIME_ZONE = 'UTC'

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter'
    ],
}
