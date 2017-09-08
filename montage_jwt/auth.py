from django.contrib.auth.models import User
from rest_framework import authentication
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from jwt import decode
from jwt.exceptions import InvalidTokenError

class JWTAuthentication(authentication.BaseAuthentication):

    _decode_options = {
        'verify_aud': False,
    }

    def authenticate(self, request):
        if 'AUTHORIZATION' not in request.META:
            return None, None

        
        auth_header = request.META['AUTHORIZATION']

        if not auth_header.startswith(api_settings.AUTH_HEADER_PREFIX + ' '):
            # Malformed header
            return None, None

        token_loc = len(api_settings.AUTH_HEADER_PREFIX) + 1
        token = auth_header[token_loc:]

        try:
            claims = decode(
                token, 
                api_settings.PUBLIC_KEY, 
                algorithms=api_settings.ALGORITHM, 
                options=self._decode_options
            )
        except InvalidTokenError:
            return None, token

        jwt = JWT.objects.get_from_claims(claims)

        if jwt.revoked:
            return None, jwt

        return jwt.user, jwt
