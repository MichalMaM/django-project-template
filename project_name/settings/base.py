from os.path import join, dirname, pardir, abspath

PROJECT_ROOT = abspath(join(dirname(__file__), pardir))
DEV_TMP_DIR = join(PROJECT_ROOT, pardir, '.devtmp')

DEBUG = False
TEMPLATE_DEBUG = False
DEBUG_STYLES = False
DEBUG_SCRIPTS = False
DEBUG_TOOLBAR = False
DEBUG_THUMBNAIL = False
DEBUG_URLS = False

ADMINS = ()
MANAGERS = ADMINS

# new Django security settings
ALLOWED_HOSTS = []

# NOTE: development settings, overwrite it in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(DEV_TMP_DIR, 'devel.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# NOTE: development settings, overwrite it in production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

DATE_FORMAT = 'j. n. Y'

DATETIME_FORMAT = '%s %s' % (DATE_FORMAT, 'H:i')

# Media and static settings, development
MEDIA_ROOT = join(DEV_TMP_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(DEV_TMP_DIR, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    join(PROJECT_ROOT, 'project_static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# NOTE: development settings, use real secret key in your production
SECRET_KEY = '{{ secret_key }}'

# NOTE: this is development, define cached loaders in production settings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)

# TODO: what we really need?
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    #'django.core.context_processors.request',
    # static/media url, debug variables etc.
    '{{ project_name }}.context_processors.settings_variables',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    #'grappelli.dashboard',
    #'grappelli',
    'django.contrib.admin',

    'south',

    #'taggit',

    '{{ project_name }}',

    'sorl.thumbnail',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365
SESSION_COOKIE_DOMAIN = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'handlers': ['file'],
        'level': 'WARNING',
    },
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(asctime)s\t%(name)s\t%(lineno)s\t%(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/tmp/{{ project_name }}.log',
            'formatter': 'default',
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
#THUMBNAIL_ORIENTATION = False

# GRAPPELLI_ADMIN_TITLE = "{{ project_name }} admin %s" % PROJECT_VERSION
# GRAPPELLI_INDEX_DASHBOARD = '{{ project_name }}.dashboard.CustomIndexDashboard'
