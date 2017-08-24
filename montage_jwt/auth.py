from django.contrib.auth.models import User

from rest_framework import authentication
from rest_framework import exceptions

from .settings import api_settings
from .models import JWT

import jwt
from jwt.exceptions import InvalidTokenError

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('AUTHORIZATION')

        pub_key = api_settings.PUBLIC_KEY

        claims = JWT.decode(token)
        try:
            claims = jwt.decode(token, pub_key)
        except InvalidTokenError:
            return None


        jwi = claims['jwi']
        try:
            JWT.objects.get(pk=jwi)
        username = claims['sub'] 
