"""
WSGI config for brick project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from configurations.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
