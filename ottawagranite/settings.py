# Django settings for ottawagranite project.
# Local settings override at end of file

DEBUG = True
TEMPLATE_DEBUG = DEBUG
import dj_database_url
import os

projdir = os.path.abspath(os.path.dirname(__file__))
PROJDIR = projdir

ADMINS = (
    ('Michael Soulier', 'msoulier@digitaltorque.ca'),
    ('Paul Shannon', 'paul@paulshannon.ca')
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://ottawagranite_user:default@localhost/ottawagranite'
        )
    }

# The model to use for additional user data.
AUTH_PROFILE_MODEL = 'membership.Member'

SOUTH_DATABASE_ADAPTERS = {'default': 'south.db.postgresql_psycopg2'}  # http://stackoverflow.com/a/15286449/460877

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# For Django-registration
ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_OPEN = True

# For email sending
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'do-not-reply@digitaltorque.ca')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL',
                                    'do-not-reply@digitaltorque.ca')
EMAIL_USE_TLS = False
if os.environ.has_key('EMAIL_USE_TLS') and os.environ['EMAIL_USE_TLS'] == 'yes':
    EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', 'thawing-inlet-5759.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(projdir, "../static"))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(projdir, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'woedg-p-%e&5pg_i^8#=m%^tjwc89vvr&ka8$q++gq7*isb6u%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ottawagranite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ottawagranite.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(projdir, "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'gunicorn',
    'south',
    'curling',
    'finance',
    'membership',
    'ottawagranite',
    'gunicorn',
    'registration',
    'django_extensions'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
