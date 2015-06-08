# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
'''

import os

from configurations import values
from django.utils.crypto import get_random_string
from .common import Common


class Local(Common):

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG

    SECRET_KEY = os.environ.get(
        "SECRET_KEY", get_random_string(50, (
            "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")))

    TWITTER_KEY = values.Value()
    TWITTER_SECRET = values.Value()
    TWITTER_TOKEN = values.Value()
    TWITTER_TOKEN_SECRET = values.Value()
