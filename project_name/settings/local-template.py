from os.path import exists
from {{ project_name }}.settings.base import DEV_TMP_DIR, DATABASES, CACHES, INSTALLED_APPS, MIDDLEWARE_CLASSES, LOGGING

# check tmp directory exists or create
if not exists(DEV_TMP_DIR):
    from os import makedirs
    makedirs(DEV_TMP_DIR)

DEBUG = True
TEMPLATE_DEBUG = True
DEBUG_STYLES = True
DEBUG_SCRIPTS = True
DEBUG_TOOLBAR = False
DEBUG_THUMBNAIL = True
DEBUG_URLS = True

SESSION_COOKIE_DOMAIN = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

_DATABASES ={
    'pgsql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
    },
}

CACHES.update({
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
})

LOGGING['root']['handlers'] = ['console']

if DEBUG_TOOLBAR:
    import cache_toolbar.panels.redis
    INSTALLED_APPS += (
        'debug_toolbar',
        'cache_toolbar',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': False,
        'INTERCEPT_REDIRECTS': False,
    }

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        'cache_toolbar.panels.BasePanel',
    )

    INTERNAL_IPS = ('127.0.0.1',)
