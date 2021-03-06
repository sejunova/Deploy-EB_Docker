"""
Django settings for instagram project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os
import raven

# paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')

# Media paths
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

# Static paths
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# config paths
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEV = os.path.join(CONFIG_SECRET_DIR, 'settings_dev.json')
CONFIG_SECRET_DEPLOY = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON).read())

# Facebook related configuration
FACEBOOK_APP_ID = config_secret_common['facebook']['app_id']
FACEBOOK_APP_SECRET_CODE = config_secret_common['facebook']['secret_code']
FACEBOOK_SCOPE = ['user_friends', 'public_profile', 'email']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'storages',
    'rest_framework',
    'rest_framework.authtoken',

    'corsheaders',

    'raven.contrib.django.raven_compat',

    'post',
    'member',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Template
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'member.backends.FacebookBackend',
]

AUTH_USER_MODEL = 'member.User'
LOGIN_URL = 'member:login'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CORS_ORIGIN_WHITELIST = (
    'localhost:3001',
)
RAVEN_CONFIG = {
    'dsn': 'https://14223119b0d64591b8c4ccdc11061c0f:a3ba4c92fb4b4796bf70157a3c6461e8@sentry.io/248306',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
