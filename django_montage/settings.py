"""
Django settings for django_montage project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

This file contains defaults for many settings, but all can be overwritten in
prod_settings.py or dev_settings.py.
"""


# This file holds configurations that are required for this project.
# However, all of these can and should be overwritten in local_settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q!gh$o-pe@+_5xbc3ho@hyy0w^-k*2c9kshkj_kt@qju22cczy'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'registration', # "Should be immediately above 'django.contrib.auth'" from
                    # registration docs
                    # https://django-registration-redux.readthedocs.io/en/latest/quickstart.html#settings
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rafter_user_service',
    'rest_framework',
    'montage_ui',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Needed for JWT
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_montage.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication', # Allow JWT Auth
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # For app templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django_settings_export.settings_export',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# List of allowed hosts
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'django_montage.wsgi.application'

### JWT settings

from datetime import timedelta

JWT_AUTH = {
    'JWT_ALGORITHM': 'RS512',
    'JWT_EXPIRATION_DELTA': timedelta(hours=3),
    # Overwrite this key pair in production.
    'JWT_PRIVATE_KEY': '''-----BEGIN PRIVATE KEY-----
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
ccqYitd/WHYJESS302ZRA9ciMiIoxKs=
-----END PRIVATE KEY-----''',
    'JWT_PUBLIC_KEY': '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA7OhUedJrcB+97WVOQ6Q0
BBVR+c9OzLOQGWN/qBLsRoVKtZrfWBMgCDJQ3vQnWn80KfBR2mDZXbuSfd380EwW
QsKlK/5TUFHQjpOFxSIHsLJzR9isVEyumQzYzofbdw1L2GBQPk1yaACPckaNi5vt
QCGrD7hIKpq9DsmO9wPYZOvAlna+qW52zkgkzYd3oKwf0aWIYpIpFPtDwP0V58Sb
8CZ+7Ji9CyK0lLDZ2zolEpPFtT5bDvtdEDR9U88/cx1W5b6ip2VidkcZfHwSwy/G
jdxYd16Nnhsrie6OwefXk19WiJ9SNLW+ofmyfqsgEfV6+21JMg5Odb6wc7Ft+6lI
orL04hGVJyN1+wgXne47KUzpOOplx3i7ztiQYsT2QiqU0fgLf9HEWzclE7RmiNgF
hs8y/UE5V/DLyuWSp0nSNodQSdD9LEJmg+o7pHHciGvufA+aI9uDsVLac3ZLgCEz
IHfkgEr4V76QQJ8GvvQZkKoKMCpS34ygutGD+8RJTkHap+Mo/lOb0ytCmormFUCC
IqulTJNZUkcNdxTFM+1iaQvJHSG0wr2ktJUlMpPXSVTtCWywWwdP2vEeWGSITETB
iwmMxrWj0/KKEgmOznXDocnvQvqpXDnrf6CT6IV5+GbJOLhZKG3HaTWw1Cy68Ecd
ot3hXnxVVLBc7wwVYgpj/GsCAwEAAQ==
-----END PUBLIC KEY-----''',
}

### Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

### Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

### Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

### Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

### Login configuration

LOGIN_URL = 'auth_login'
LOGIN_REDIRECT_URL = '/'

### Registration settings

# List of admins for the registration app
ADMINS = [] # Will need to overwrite ADMINS for registration
ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_OPEN = True

# Email backend to console for user activation
# By default we should use the console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

### Settings Export
SETTINGS_EXPORT = [
    # ...
    'DEBUG'
]


try:
    from .local_settings import *
    print('Loaded local_settings.py.')
except ImportError:
    print('local_settings.py not found, using defaults.')
