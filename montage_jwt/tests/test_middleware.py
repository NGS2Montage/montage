from django.test import TestCase
from unittest.mock import Mock

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from django.utils import timezone
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from montage_jwt.util import make_claims
from montage_jwt.middleware import TokenMiddleware
from datetime import timedelta
from .utils import set_key_pair
import os

def get_response(request):
    return None

class TokenMiddlewareTest(TestCase):

    # Setup
    @classmethod
    def setUpClass(cls):
        super(TokenMiddlewareTest, cls).setUpClass()
        set_key_pair()

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.request = self.make_request()
        self.middleware = TokenMiddleware(get_response)

    # Helper Methods
    def make_request(self):
        request = Mock()
        request.session = {}
        return request

    def get_outdated_token(self):
        claims = make_claims(self.user, 'LOG')
        now = timezone.now()
        a_while_ago = now - timedelta(hours=3)
        claims['iat'] = a_while_ago
        claims['nbf'] = a_while_ago
        claims['exp'] = now - timedelta(seconds=1)
        return JWT.objects.create_token(claims, self.user)

    def get_not_outdated_token(self):
        claims = make_claims(self.user, 'LOG')
        return JWT.objects.create_token(claims, self.user)

    # Tests
    def test_refresh_middleware_no_refresh(self):
        request = self.make_request()
        request.user = self.user
        jwt = self.get_not_outdated_token()
        request.session['JWT'] = jwt.token

        self.middleware(request)

        new_jwt = JWT.objects.get_model_from_token(request.session['JWT'])

        self.assertEqual(jwt, new_jwt)

    def test_refresh_middleware_with_refresh(self):
        request = self.make_request()
        request.user = self.user
        jwt = self.get_outdated_token()
        request.session['JWT'] = jwt.token

        self.middleware(request)

        new_jwt = JWT.objects.get_model_from_token(request.session['JWT'])

        self.assertNotEqual(jwt, new_jwt)

    def test_middleware_adds_token(self):
        request = self.make_request()
        request.user = self.user

        self.assertNotIn('JWT', request.session)

        self.middleware(request)

        self.assertIn('JWT', request.session)
