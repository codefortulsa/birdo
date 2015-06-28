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

    INSTALLED_APPS += ("djangosecure", )

    GEOS_LIBRARY_PATH = values.Value('', environ_prefix=False)
    GDAL_LIBRARY_PATH = values.Value('', environ_prefix=False)
    PROJ4_LIBRARY_PATH = values.Value('', environ_prefix=False)
