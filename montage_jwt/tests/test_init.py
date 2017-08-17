from django.test import TestCase

from django.contrib.auth.models import User

from montage_jwt.util import make_token
from montage_jwt.settings import api_settings
import os

class TokenTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TokenTest, cls).setUpClass()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        p_key_file = dir_path + '/private.pem'

        with open(p_key_file, 'r') as f:
            p_key = f.read().strip()

        api_settings.PRIVATE_KEY = p_key

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')

    def test_token_create(self):
        token = make_token(self.user, 'LOG')
