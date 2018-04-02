from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
set_config(secrets, module_name=__name__, start=True)
# print(getattr(sys.modules[__name__], 'DATABASES'))

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com'
]
WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

# STATICFILES_STORAGE = 'config.storage.StaticFileStorage'
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'