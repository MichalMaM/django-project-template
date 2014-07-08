"""
Project settings are separated to
base.py  - basic application specific settings
local.py - settings specific to an installation (this should never be saved in repository)
"""
import sys

from {{ project_name }} import __versionstr__
from {{ project_name }}.settings.base import *

SERVER_CONFIGURATION_FILE = '/usr/local/etc/pyconfs/{{ project_name }}/'

# server-specific settings
sys.path.insert(0, SERVER_CONFIGURATION_FILE)
try:
    from {{ project_name }}_conf import *
except ImportError:
    pass
finally:
    del sys.path[0]

# finally local settings overides all
# overrides anything
try:
    from {{ project_name }}.settings.local import *
except ImportError:
    pass

#append package version to STATIC_URL to invalidate old statics
VERSION_STAMP = __versionstr__.replace(".", "")
STATIC_URL = '%sversion%s/' % (STATIC_URL, VERSION_STAMP)

# try to bump cache version by project version
try:
    CACHES['default']['VERSION'] = VERSION_STAMP
except KeyError:
    pass
