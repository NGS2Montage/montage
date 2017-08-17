from datetime import timedelta

default_app_config = 'montage_jwt.apps.MontageJwtConfig'

DEFAULT_TOKEN_TYPE_TABLE = {
    'LOG': ('login', timedelta(hours=5)),
    'API': ('api', timedelta(days=5)),
    'CPU': ('compute', timedelta(days=5)),
}
