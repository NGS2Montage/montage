from django.contrib.auth.models import User

from rest_framework import authentication
from rest_framework import exceptions

from .settings import api_settings
from .models import JWT

import jwt
from jwt.exceptions import InvalidTokenError

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        raise NotImplementedError('auth not written yet')
