import jwt
import uuid
from datetime import datetime, timedelta
from .settings import api_settings
from .models import Token

default_app_config = 'montage_jwt.apps.MontageJwtConfig'

def make_token(user, jwt_type):
    claims = make_claims(user, jwt_type)
    token = jwt.encode(claims, api_settings.PRIVATE_KEY, algorithm='RS512').decode('utf-8')
    return Token.objects.create(jwi=claims['jwi'], token=token, scope=jwt_type, user=user)

def make_claims(user, jwt_type, nbf=None):
    if jwt_type not in api_settings.TOKEN_TYPE_TABLE:
        raise ValueError('Token type: {} is undefined.'.format(jwt_type))

    jwi = uuid.uuid4()
    iat = datetime.utcnow()
    exp = iat + get_exp_delta(jwt_type)
    username = user.get_username()
    iss = this_uri()
    aud = get_aud(user)
    claims = {
        'jwi': str(jwi),
        'scope': jwt_type,
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

def get_exp_delta(jwt_type):
    return timedelta(hours=3)

def get_aud(user):
    return []

def refresh_token(token):
    print('refreshing')
    return token

def get_jwi(token):
    claims = jwt.decode(token, verify=False)
    return claims['jwi']
