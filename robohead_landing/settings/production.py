from __future__ import absolute_import, unicode_literals

import os
import dj_database_url
from distutils.util import strtobool

from .base import *

INSTALLED_APPS += ('anymail', )

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get(
        'MAILGUN_API_KEY', '<your Mailgun key>'),
}

DEBUG = bool(strtobool(os.environ.get('DEBUG', 'True')))

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

SECRET_KEY = os.environ.get('SECRET_KEY', '<change_me>')

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'example.com').split(',')

try:
    from .local import *
except ImportError:
    pass
