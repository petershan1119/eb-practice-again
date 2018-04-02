from urllib.request import urlopen

from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
set_config(secrets, module_name=__name__, start=True)
# print(getattr(sys.modules[__name__], 'DATABASES'))

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.sangwonhan.com'
]


def is_ec2_linux():
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False


def get_linux_ec2_private_ip():
    if not is_ec2_linux():
        return None
    try:
        response = urlopen("http://169.254.169.254/latest/meta-data/local-ipv4")
        ec2_ip = response.read().decode('utf-8')
        if response:
            response.close()
        return ec2_ip
    except Exception as e:
        print(e)
        return None

private_ip = get_linux_ec2_private_ip()
if private_ip:
        ALLOWED_HOSTS.append(private_ip)


WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'storages',
]

# STATICFILES_STORAGE = 'config.storage.StaticFileStorage'
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'