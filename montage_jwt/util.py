import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from .settings import api_settings
from montage_jwt.models import JWT
from functools import wraps
from django.urls import reverse
import jwt

default_app_config = 'montage_jwt.apps.MontageJwtConfig'
table = api_settings.TOKEN_TYPE_TABLE

def make_login_token(user):
    claims = make_claims(user, 'LOG')
    jwt = JWT.objects.create_token(claims, user)
    return jwt

def make_claims(user, scope, nbf=None):
    if scope not in api_settings.TOKEN_TYPE_TABLE:
        raise ValueError('Token type: {} is undefined.'.format(scope))

    jwi = uuid.uuid4()
    iat = timezone.now()
    exp = iat + get_exp_delta(scope)
    username = user.get_username()
    iss = reverse('montage_jwt:public_key')
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

def get_jwi(token):
    if isinstance(token, JWT):
        return token.jwi
    else:
        claims = jwt.decode(token, api_settings.PUBLIC_KEY, algorithms=api_settings.ALGORITHM)

def get_exp_delta(scope):
    exp_delta = table[scope][1]
    return exp_delta

def get_aud(user):
    # For now, the audience is always the same...
    return ['@core', '#public']

def refresh(claims):
    new_claims = {
        'jwi': str(uuid.uuid4()),
        'exp': timezone.make_aware(datetime.utcfromtimestamp(claims['exp']) + get_exp_delta(claims['scope'])),
        'orig_iat': claims['iat'],
        'iat': timezone.now(),
    }

    claims.update(new_claims)
    return JWT.objects.create_token(claims)

def decode(token):
    # For now we don't need to verify the audience because these tokens don't
    # authenticate against us.
    options = {
        'verify_aud': False,
    }

    claims = jwt.decode(
        token, 
        api_settings.PUBLIC_KEY, 
        algorithms=api_settings.ALGORITHM,
        options=options
    )

    return claims
