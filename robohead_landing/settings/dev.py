from __future__ import absolute_import, unicode_literals

from .base import *

INSTALLED_APPS += ('wagtail.contrib.wagtailstyleguide', )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nmy4=t$okv$3v4kkpd*n2+91jm3#cu0e)-$_6w@$_i_ohnygsq'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
