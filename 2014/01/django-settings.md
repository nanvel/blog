labels: Blog
        Django
created: 2014-01-12T00:00

# Django settings

I saw a lot of times when newbies in Django have problems in editing Django settings. I hope this post will be useful for them. The post shows example of django settings I use.

First of all, I split settings into few files. Instead of settings.py we will have settings directory contains few settings files and ```__init__.py```.

Files tree:
```text
- myproject
    - settings
        - __init__.py
        - utils.py
        - admins.py
        - default.py
        - db.py
        - media.py
        - apps.py
        - local.py.default
```

```__init__.py```:
```python
from .admins import *
from .default import *
from .db import *
from .media import *
from .apps import *

try:
    from local import *
except ImportError:
    pass
```

```utils.py```:
```python
import os.path


SETTINGS_ROOT = os.path.dirname(os.path.realpath(__file__))
rel = lambda p: os.path.join(SETTINGS_ROOT, '../..', p)
```

```admins.py```:
```python
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
```

```default.py```:
```python
from .utils import rel


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-u&g%3b$3g=-(#iDD=e7i5q7!0mv71!-enbq6uu8_bf*dz+&YY'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    rel('myproject/templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

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
```

```db.py```:
```python
from .utils import rel


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('db.sqlite3'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
```

```media.py```:
```python
from .utils import rel


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = rel('myproject/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = rel('myproject/media/static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    rel('myproject/static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
```

```MEDIA_URL``` - url where media files will be available (on production should be in sync with web server config).

```MEDIA_ROOT``` - path to directory where media files will be stored,

```STATIC_URL``` - url where static files will be available (on production should be in sync with web server config).

```STATIC_ROOT``` - path to directory static files will be copied to (on collectstatic management command call, not required while ```DEBUG == True```).

To serve media files without real web server (while development), add next lines to project urls:

```python
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
```

```apps.py```:
```python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'portfolio.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'south',

    'myproject.apps.myapp',
)
```

```local.py.default```:
```python
from .utils import rel

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('db.sqlite3'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

SECRET_KEY = '-u&g%3b$3g=-(#iDD=e7i5q7!0mv71!-enbq6uu8_bf*dz+&YY'

# MEDIA_ROOT = ''
# STATIC_ROOT = ''
```

```local.py``` should be added to ```.gitignore```.

Place: Phuket, Thailand
