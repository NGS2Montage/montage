from django.conf import settings
from rest_framework.settings import APISettings
from datetime import timedelta

USER_SETTINGS = getattr(settings, 'MONTAGE_JWT', None)

DEFAULTS = {
    'PRIVATE_KEY': None,
    'PUBLIC_KEY': None,
    'ALGORITHM': 'RS512',
    'AUTH_HEADER_PREFIX': 'JWT',
    'TOKEN_TYPE_TABLE': 'montage_jwt.DEFAULT_TOKEN_TYPE_TABLE',
    'REFRESH_THRESHOLD': timedelta(minutes=10),
}

# These settings will be imported by python
IMPORT_STRINGS = {
    'TOKEN_TYPE_TABLE',
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
