"""
Django settings for QUIRUSTETIC project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
from django.urls import reverse_lazy

import dj_database_url

from decouple import config

import os

import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dt82=dpm!yrk3dmcc)v8_y+zn1#me3dj&f0b6peq6d4=zgvo+5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion',
    'intercoolerjs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'QUIRUSTETIC.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 './templates',
                 os.path.join(PROJECT_PATH, 'todo_list','templates'),
                 os.path.join(PROJECT_PATH, 'gestion','templates'),
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

WSGI_APPLICATION = 'QUIRUSTETIC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
        # 'default': {
           # 'ENGINE': 'django.db.backends.sqlite3',
           # 'NAME': 'database.db',
           # 'USER': 'root',
           # 'PASSWORD': '96020917463',
           # 'HOST':'127.0.0.1',
           # 'PORT':'3307',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'quirustetic$quirustetic',
        # 'OPTIONS':{'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        # 'USER': 'quirustetic',
        # 'PASSWORD': 'Itm733922',
        # 'HOST':'quirustetic.mysql.pythonanywhere-services.com',
        #  'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #  'NAME': 'gestionequipos',
        #  'USER': 'postgres',
        #  'PASSWORD': '96020917463',
        #  'HOST': 'localhost',
        #  'PORT': '',
        'default': dj_database_url.config(
        default=config('DATABASE_URL')),
    #)
    }
#}
#DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGIN_URL=reverse_lazy('login')
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-Co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
handler404 = 'gestion.views.handler404'
handler500 = 'gestion.views.handler500'
#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
#EMAIL_HOST = 'secure.serverfoo.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = '96020917463'
EMAIL_HOST_USER = 'gestioningenieriabiomedica@gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
try:
    from local_settings import *
except ImportError:
    pass


