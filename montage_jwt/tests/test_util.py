from django.test import TestCase
from django.contrib.auth.models import User
from montage_jwt.util import make_claims
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from datetime import datetime, timedelta
import os

class JWTTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(JWTTest, cls).setUpClass()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        p_key_file = dir_path + '/private.pem'

        with open(p_key_file, 'r') as f:
            p_key = f.read().strip()

        api_settings.PRIVATE_KEY = p_key

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')

    def test_token_create_no_user(self):
        claims = make_claims(self.user, 'LOG')
        jwt = JWT.objects.create_token_from_claims(claims)
