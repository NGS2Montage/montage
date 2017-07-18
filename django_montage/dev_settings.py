from .base_settings import *

# Add development settings here
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q!gh$o-pe@+_5xbc3ho@hyy0w^-k*2c9kshkj_kt@qju22cczy'

# List of allowed hosts
ALLOWED_HOSTS = []

### Registration settings

# List of admins
ADMINS += ['admin']
# ADMINS += ['YOUR_DJANGO_SUPERUSER']

# Email backend to console for user activation
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

### JWT SETTINGS
# Default location for key is in the project root
try:
    with open(BASE_DIR + '/private.pem', 'r') as f:
        PRIVATE_KEY = f.read().strip()

    with open(BASE_DIR + '/public.pem', 'r') as f:
        PUBLIC_KEY = f.read().strip()

    JWT_AUTH['JWT_PUBLIC_KEY'] = str(PUBLIC_KEY)
    JWT_AUTH['JWT_PRIVATE_KEY'] = str(PRIVATE_KEY)
except:
    print('Could not find ./private.pem or ./public.pem.')
