"""

WSGI config for odm2cvs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
print os.environ
sys.path.append(os.environ["ODM2CVS_PROJECT_ROOT"])
#sys.path.append('/home/denver/projects/ODM2/src/odm2cvs')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "odm2cvs.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
