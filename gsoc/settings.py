"""
Django settings for gsoc project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import logging.config
import django.utils.timezone as tz
import os
import datetime

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ngo5cy%zk_8g_sw%%7vc3(xn4pjm(zuu1!nvff!iri1cwa2)@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1',)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.1/ref/settings/#email
# TODO: Update it with real settings
ADMINS = [('Admin 1', 'placeholder@python-gsoc.org')]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[Python-GSoC] '
if DEBUG:
    EMAIL_USE_TLS = True
    SERVER_EMAIL = 'psfgsoctestmail@airmail.cc'
    EMAIL_HOST = 'mail.cock.li'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "psfgsoctestmail@airmail.cc"
    EMAIL_HOST_PASSWORD = "psfgsoctestmail"
else:
    DEFAULT_FROM_EMAIL = 'placeholder@python-gsoc.org'
    EMAIL_USE_TLS = True
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "realemail@realdomain.tld"
    EMAIL_HOST_PASSWORD = "supersecretpassword"
# Application definition
ROOT_URLCONF = 'gsoc.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'gsoc', 'static'),
)
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gsoc', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'djangocms_text_ckeditor',
    'djangocms_history',
    'easy_thumbnails',
    'filer',
    'djangocms_audio',
    'djangocms_video',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_column',
    'djangocms_link',
    'djangocms_style',
    'djangocms_snippet',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    'gsoc',
    'debug_toolbar'
)
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('homepage.html', 'Homepage'),
    ('gettingstarted.html', 'Getting Started'),
    ('ideas.html', 'Project Ideas'),
    ('mentors.html', 'Mentors'),
    ('schedule.html', 'Schedule'),
    ('students.html', 'Students'),
    ('contact.html', 'Contact'),
    ('myprofile.html', 'My Profile'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    },
    'auth_db': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'users.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    },
}

DATABASE_APPS_MAPPING = {
    'auth': 'auth_db',
    'admin': 'auth_db',
    'sessions': 'auth_db',
}

DATABASE_ROUTERS = ['gsoc.router.DatabaseAppsRouter']

MIGRATION_MODULES = {

}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/after-login/'

# AUTH_USER_MODEL = 'gsoc.User'

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See: http://docs.djangoproject.com/en/dev/topics/logging
# See: https://docs.djangoproject.com/en/2.1/topics/logging/#disabling-logging-configuration
LOGGING_CONFIG = None

if DEBUG:
    ERROR_LEVEL = 'DEBUG'
else:
    ERROR_LEVEL = 'INFO'

ERROR_HANDLERS = ['file', 'mail_admins']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s %(process)d '
                       '%(thread)d %(filename)s %(module)s %(funcName)s '
                       '%(lineno)d %(message)s')
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/pygsoc.log'),
            'formatter': 'verbose',
            'when': 'midnight',
            'backupCount': 60,
            'encoding': 'utf-8',
        },
        'access_logs': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/access.log'),
            'formatter': 'simple',
            'when': 'midnight',
            'backupCount': 7,
            'encoding': 'utf-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['file'],
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ERROR_HANDLERS,
            'level': ERROR_LEVEL,
        }
    }
}
logging.config.dictConfig(LOGGING)

# Runcron settings

RUNCRON_NUM_WORKERS = 5
RUNCRON_TIMEOUT = 10

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']
DJANGOCMS_VIDEO_ALLOWED_EXTENSIONS = ['mp4', 'webm', 'ogv']

# Ckeditor settings

CKEDITOR_SETTINGS = {
    'disableNativeSpellChecker': False,
    'language': '{{ language }}',
    'extraPlugins': 'button,clipboard,dialog,dialogui,image2,lineutils,notification,toolbar,widget,widgetselection,youtube',
    'toolbar': [
        {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
        # ['cmsplugins', 'cmswidget'],
        {'name': 'settings', 'items': ['Source', 'ShowBlocks', 'Maximize']},
        '/',
        {'name': 'basicstyles',
         'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting',
                   'RemoveFormat']},
        {'name': 'paragraph',
         'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                   'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
        {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        {'name': 'insert', 'items': ['Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Image', 'Youtube']},
        '/',
        {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
        {'name': 'colors', 'items': ['TextColor', 'BGColor']},
    ],
    'toolbarCanCollapse': False,
}

TEXT_ADDITIONAL_TAGS = ('iframe',)

# IRC CommandBot settings

BOT_NICK = "CommandBot"
IRC_SERVER = "irc.freenode.org"
RECEIVER = "limnoria"

# Disable page cache so that CSRF token can be updated
CMS_PAGE_CACHE = False

