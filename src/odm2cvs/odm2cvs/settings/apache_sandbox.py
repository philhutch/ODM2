from odm2cvs.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_ROOT = os.environ['ODM2CVS_STATIC_ROOT']
STATIC_URL = '/static/'
SITE_URL = ''