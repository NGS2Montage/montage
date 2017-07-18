from .base_settings import *

# Add production settings here

### Allowed hosts
ALLOWED_HOSTS += []

### Registration settings
# Registration requires admins to send activation emails to.
# ADMINS += ['SUPERUSER']

### Email Settings
# See django docs.
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-backend

### JWT Settings
# Must set the public and private key to an RSA key pair.  These can be read
# from a file or just put in this file. They just need to be strings and need
# to be a key pair.
JWT_AUTH['JWT_PUBLIC_KEY'] = 'PUBLIC KEY'
JWT_AUTH['JWT_PRIVATE_KEY'] = 'PRIVATE KEY'


