"""
Django settings for birdo project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

For the configurations module and it's values, see
https://github.com/jezdez/django-configurations
"""

from os.path import dirname, abspath, join

from configurations import Configuration, values


class Common(Configuration):

    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    BASE_DIR = dirname(dirname(abspath(__file__)))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'vhmc9lo887c)w%dum0oln(!wof(m#+f5$j8p#%&v=(3946n2ht'

    # SECURITY WARNING: don't run with debug turned on in production!
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG

    ALLOWED_HOSTS = []

    # APP CONFIGURATION
    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.gis',
    )

    # Third-party apps, patches, fixes
    THIRD_PARTY_APPS = (
        'mptt',
        'django_mptt_admin',
        'django_extensions',
        'rest_framework',
        'webpack_loader',
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'birds',
        'shares',
        'api',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'birdo.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'birdo.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    # https://github.com/kennethreitz/dj-database-url

    DATABASES = values.DatabaseURLValue('postgis://birdo_user@localhost/birdo')

    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = False

    USE_L10N = False

    USE_TZ = False

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_ROOT = join(BASE_DIR, 'static')
    STATIC_URL = values.Value('/static/')
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    MEDIA_ROOT = join(BASE_DIR, 'media/')
    MEDIA_URL = values.Value("/media/")

    # Social Network settings

    TWITTER_KEY = values.SecretValue()
    TWITTER_SECRET = values.SecretValue()
    TWITTER_TOKEN = values.SecretValue()
    TWITTER_TOKEN_SECRET = values.SecretValue()

    # Rest framework settings

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        ),
        'DEFAULT_PAGINATION_CLASS': 'api.pagination.BirdoPagination',
    }

    # Templates

    # List of processors used by RequestContext to populate the context.
    # Each one should be a callable that takes the request object as its
    # only parameter and returns a dictionary to add to the context.
    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        # "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.debug",
        # "django.core.context_processors.i18n",
        "django.core.context_processors.static",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        # "django.core.context_processors.tz",
    )

    TEMPLATES = [
        {
            "BACKEND": "django_jinja.backend.Jinja2",
            "APP_DIRS": True,
            "OPTIONS": {
                "match_extension": ".jinja",
                "match_regex": r"^(?!admin|debug_toolbar/).*",
                "newstyle_gettext": True,
                "extensions": [
                    # "jinja2.ext.do",
                    # "jinja2.ext.loopcontrols",
                    # "jinja2.ext.with_",
                    "jinja2.ext.i18n",
                    # "jinja2.ext.autoescape",
                    # "django_jinja.builtins.extensions.CsrfExtension",
                    # "django_jinja.builtins.extensions.CacheExtension",
                    # "django_jinja.builtins.extensions.TimezoneExtension",
                    # "django_jinja.builtins.extensions.UrlsExtension",
                    # "django_jinja.builtins.extensions.StaticFilesExtension",
                    # "django_jinja.builtins.extensions.DjangoFiltersExtension",
                    # "django_jinja.builtins.extensions.DjangoExtraFiltersExtension",
                    "webpack_loader.contrib.jinja2ext.WebpackExtension",
                ],
                "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
                "autoescape": True,
                "auto_reload": DEBUG,
                "translation_engine": "django.utils.translation",
            }
        },
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": TEMPLATE_CONTEXT_PROCESSORS
            },
        },
    ]

    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     }
    # }

    # Webpack
    WEBPACK_LOADER = {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': abspath(BASE_DIR + '/birds/assets/webpack-stats.json')
    }

    # Place bcrypt first in the list, so it will be the default password hashing
    # mechanism
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    )

    # Mail settings
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    EMAIL_HOST = values.Value('localhost')
    EMAIL_PORT = values.IntegerValue(1025)
    EMAIL_HOST_USER = values.Value('')
    EMAIL_HOST_PASSWORD = values.Value('')
    # End mail settings
