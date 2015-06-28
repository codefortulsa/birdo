# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
'''
from configurations import values

from .common import Common


class Production(Common):

    INSTALLED_APPS = Common.INSTALLED_APPS

    SECRET_KEY = values.SecretValue()


    GEOS_LIBRARY_PATH = values.Value('', environ_prefix=False)
    GDAL_LIBRARY_PATH = values.Value('', environ_prefix=False)
    PROJ4_LIBRARY_PATH = values.Value('', environ_prefix=False)

    ALLOWED_HOSTS = ['birdo.destos.com', '.destos.com']

    # django-secure
    # This ensures that Django will be able to detect a secure connection
    # properly on Heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Django secure disabled for now
    # INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    INSTALLED_APPS += ("gunicorn", )

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    # Mail settings
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    ADMINS = values.SingleNestedTupleValue()
