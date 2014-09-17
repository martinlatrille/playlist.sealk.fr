"""
WSGI config for playlist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import sys
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playlist.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
application = Cling(get_wsgi_application())
