"""
WSGI config for recepty project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

django_settings_module = '{{ project_name }}.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = django_settings_module

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from raven.contrib.django.middleware.wsgi import Sentry
application = Sentry(application)
