import os

from django.contrib import messages


# =================================================================================
# DIRECTORY DEFINITIONS
# =================================================================================

_THIS_DIR = os.path.dirname(__file__)

# home dir is the root web_src directory
HOME_DIR = os.path.abspath(os.path.dirname(_THIS_DIR))
PROJECT_DIR = os.path.join(HOME_DIR, 'example_project')

# live dir is the directory that will host uploaded files and generated css/javascript when running in prod
LIVE_DIR = os.environ.get('DJANGO_APP_LIVE', os.path.join(PROJECT_DIR, 'live'))

# static dir is the source of static files
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(LIVE_DIR, 'static')

# =================================================================================
# GENERAL SETTINGS
# =================================================================================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_APP_DEBUG', False)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_APP_SECRET_KEY', '!q73o$w9v)qbv72xq5!ra7yz-dn%hg5o5946mc+13qjue$@uff')

SITE_DOMAIN = os.environ.get('DJANGO_APP_SITE_DOMAIN')
ALLOWED_HOSTS = ['localhost', SITE_DOMAIN]

MESSAGE_TAGS = {messages.ERROR: 'danger'}

FIXTURE_DIRS = [
    os.path.join(HOME_DIR, 'example_project', 'fixtures')
]

# =================================================================================
# Application definition
# =================================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_fullclean',

    'example_project.apps.core',
    'example_project.apps.example_app',
    'example_project.apps.example_api',
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

ROOT_URLCONF = 'example_project.urls'

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

WSGI_APPLICATION = 'example_project.wsgi.application'

# =================================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# =================================================================================

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# =================================================================================
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# =================================================================================

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': os.environ.get('DB_CONN_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_CONN_NAME', os.path.join(LIVE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DB_CONN_USER', ''),
        'PASSWORD': os.environ.get('DB_CONN_PASSWORD', ''),
        'HOST': os.environ.get('DB_CONN_HOST', ''),
        'PORT': os.environ.get('DB_CONN_PORT', ''),
    }
}

# =================================================================================
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
# =================================================================================

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

# =================================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# =================================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =================================================================================
# Logging
# https://docs.djangoproject.com/en/1.9/topics/logging/#configuring-logging
# =================================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s.%(msecs)03d] %(levelname)s [%(name)s:%(lineno)s] [%(module)s] [PID: %(process)d] %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S'
        }
    },
    'handlers': {
        'requestsall': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LIVE_DIR, 'logs', 'requests-all.log'),
            'maxBytes': 1024 * 1024 * 100,
        },
        'badlogs': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LIVE_DIR, 'logs', 'django-warn-errs.log'),
            'maxBytes': 1024 * 1024 * 100,
        },
        'consolelog': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['requestsall'],
            'propagate': True,
        },
        '': {
            'level': 'DEBUG',
            'handlers': ['consolelog', 'badlogs']
        }
    }
}
