from __future__ import absolute_import, unicode_literals

import os
import dj_database_url

from .base import *

INSTALLED_APPS += ('anymail', )

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get(
        'MAILGUN_API_KEY', '<your Mailgun key>'),
}

DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'

SECRET_KEY = os.environ.get('SECRET_KEY', '<change_me>')

CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local import *
except ImportError:
    pass
