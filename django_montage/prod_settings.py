from .base_settings import *

# Add production settings here

### Registration settings
# Registration requires admins to send activation emails to.
# ADMINS += ['SUPERUSER']

### Email Settings
# See django docs.
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-backend

### JWT Settings
JWT_AUTH['JWT_PUBLIC_KEY'] = 'PUBLIC KEY'
JWT_AUTH['JWT_PRIVATE_KEY'] = 'PRIVATE KEY'
