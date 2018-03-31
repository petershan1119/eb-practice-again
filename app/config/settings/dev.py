from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += [
    'django_extensions',
]

set_config(secrets, module_name=__name__, start=True)
print(getattr(sys.modules[__name__], 'DATABASES'))