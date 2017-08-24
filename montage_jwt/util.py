import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from .settings import api_settings
from montage_jwt.models import JWT
from functools import wraps

default_app_config = 'montage_jwt.apps.MontageJwtConfig'

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

def get_jwi(token):
    if isinstance(token, JWT):
        return token.jwi
    else:
        claims = jwt.decode(token, api_settings.PUBLIC_KEY, algorithms='RS512')

def this_uri():
    return 'test'

def get_exp_delta(scope):
    return timedelta(hours=3)

def get_aud(user):
    return []

def needs_decode(func):
    @wraps(func)
    def decorator(token, trust=False, claims=False, *args, **kwargs):
        if claims:
            return func(token, *args, **kwargs)
        elif isinstance(token, JWT):
            # If the token is in the database, we will trust it.
            claims = token.get_claims()
            return func(claims, *args, **kwargs)
        else:
            # Otherwise, we will only trust it if 'trust' is True
            verify = not trust
            claims = jwt.decode(token, api_settings.PUBLIC_KEY, verify=verify)
            return func(claims, *args, **kwargs)

    return decorator

def checks_exp(func):
    @wraps(func)
    def decorator(token, trust=False, *args, **kwargs):

        if isinstance(token, JWT):
            return func(token.exp, *args, **kwargs)
        else:
            # Otherwise, we will only trust it if 'trust' is True
            verify = not trust
            claims = jwt.decode(token, api_settings.PUBLIC_KEY, verify=verify)

            exp = datetime.utcfromtimestamp(claims['exp'])
            exp = timezone.make_aware(exp)

            return func(exp, *args, **kwargs)

@needs_decode
def refresh(claims):
    new_claims = {
        'jwi': str(uuid.uuid4()),
        'exp': timezone.make_aware(datetime.utcfromtimestamp(claims['exp']) + get_exp_delta(claims['scope'])),
        'orig_iat': claims['iat'],
        'iat': timezone.now(),
    }

    claims.update(new_claims)
    return JWT.objects.create_token(claims)

@checks_exp
def is_expired(exp):
    now = timezone.now()
    return now > exp

@checks_exp
def is_about_to_expire(exp):
    now = timezone.now()
    return now > exp - api_settings.REFRESH_THRESHOLD 
