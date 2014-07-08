from django.conf import settings
#from django.contrib.sites.models import Site

VARIABLES = {
    'DEBUG': getattr(settings, 'DEBUG', False),
    'DEBUG_STYLES': getattr(settings, 'DEBUG_STYLES', False),
    'DEBUG_SCRIPTS': getattr(settings, 'DEBUG_SCRIPTS', False),
    'STATIC_URL': getattr(settings, 'STATIC_URL'),
    'MEDIA_URL': getattr(settings, 'MEDIA_URL'),
    #'CURRENT_SITE': Site.objects.get_current(),
}


def settings_variables(request):
    return VARIABLES
