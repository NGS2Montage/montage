from django.test import TestCase
from django.contrib.auth.models import User
from montage_jwt.util import make_claims, get_exp_delta
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from datetime import datetime, timedelta
from .utils import set_key_pair

class JWTTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(JWTTest, cls).setUpClass()
        set_key_pair()

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')

    def test_token_create_no_user(self):
        claims = make_claims(self.user, 'LOG')
        jwt = JWT.objects.create_token(claims)

    def test_get_exp_delta(self):
        scope = 'LOG'
        delta = get_exp_delta(scope)
        self.assertEqual(timedelta(hours=5), delta)
