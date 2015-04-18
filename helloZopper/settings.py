"""
Django settings for helloZopper project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pfc-i0^v=8mb31p5_(t7&=&u3qiqqe)#%7a)f_^$0_&p3s*@@f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helloZopper.urls'

WSGI_APPLICATION = 'helloZopper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


# configuring templates directory
TEMPLATE_DIRS=[os.path.join(BASE_DIR, 'templates/')]

# configuring static files directory
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

# configuring static root
STATIC_ROOT = 'staticfiles'

# configuring static storage from Whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# This is How SCIGH configures Django
ADMINS = (('Kunal Sharma', 'kunalprompt@gmail.com'))

# Configuring Authentication with MongoEngine

from mongoengine import connect

 # 104.131.95.143
_MONGODB_USER = ''
_MONGODB_PASSWD = ''
_MONGODB_HOST = '104.131.95.143'
_MONGODB_PORT = 27017
_MONGODB_NAME = 'zopper'

connect(db=_MONGODB_NAME, host=_MONGODB_HOST, port=_MONGODB_PORT, username=_MONGODB_USER, password=_MONGODB_PASSWD)

# Your Database setting. 
# Read about this setting at http://stackoverflow.com/questions/14795824/improperlyconfiguredsettings-databases-is-improperly-configured-error-when
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

# configuring csrf cookie
CSRF_COOKIE_NAME = 'ct'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_AGE = 24*60*60 # hours * minutes * seconds
CSRF_COOKIE_SECURE = True # change to False if under development

# configuring session cookie
SESSION_COOKIE_NAME = 'xs'
SESSION_COOKIE_AGE = 60*60 # minutes * seconds
SESSION_COOKIE_SECURE = True # change to False if under development


# TO check the security of your site visit - http://ponycheckup.com/
# http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only
# Django Security - http://www.marinamele.com/2014/09/security-on-django-app-https-everywhere.html
# configuring SECURITY
SECURE_SSL_REDIRECT = True # change to False if under development
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')