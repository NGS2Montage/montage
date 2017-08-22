import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from .settings import api_settings

default_app_config = 'montage_jwt.apps.MontageJwtConfig'

def make_claims(user, scope, nbf=None):
    if scope not in api_settings.TOKEN_TYPE_TABLE:
        raise ValueError('Token type: {} is undefined.'.format(scope))

    jwi = uuid.uuid4()
    iat = timezone.now()
    exp = iat + get_exp_delta(scope)
    username = user.get_username()
    iss = this_uri()
    aud = get_aud(user)
    claims = {
        'jwi': str(jwi),
        'scope': scope,
        'iat': iat,
        'exp': exp,
        'sub': username,
        'iss': iss,
        'aud': aud,
    }

    if isinstance(nbf, datetime):
        claims['nbf'] = nbf
    else:
        claims['nbf'] = claims['iat']

    return claims

def this_uri():
    return 'test'

def get_exp_delta(scope):
    return timedelta(hours=3)

def get_aud(user):
    return []

def destructive_refresh(jwt):
    new_jwt = jwt.refresh()
    jwt.delete()
    return new_jwt
