from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from montage_jwt.models import JWT
from montage_jwt.util import make_claims
from montage_jwt.auth import JWTAuthentication
from unittest.mock import Mock
from .utils import set_key_pair
import os

class AuthTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(AuthTest, cls).setUpClass()
        set_key_pair()

    def make_request(self):
        request = Mock()
        request.META = {}
        return request

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.request = self.make_request()
        self.auth = JWTAuthentication()

    def test_auth_proper_token(self):
        claims = make_claims(self.user, 'API')
        jwt = JWT.objects.create_token(claims, self.user)

        auth_header = 'JWT {}'.format(jwt.token)
        self.request.META['AUTHORIZATION'] = auth_header

        user, new_jwt = self.auth.authenticate(self.request)

        self.assertEqual(user, self.user)
        self.assertEqual(jwt, new_jwt)

    def test_invalid_token(self):
        claims = make_claims(self.user, 'API')
        claims['exp'] = timezone.now() - timedelta(seconds=30)

        jwt = JWT.objects.create_token(claims, self.user)
        self.request.META['AUTHORIZATION'] = jwt.token

        user, new_jwt = self.auth.authenticate(self.request)
        self.assertIsNone(user)

    def test_no_token(self):
        user, new_jwt = self.auth.authenticate(self.request)
        self.assertIsNone(user)
