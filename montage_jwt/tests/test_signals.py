from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from montage_jwt.util import make_login_token
from unittest.mock import Mock
from .utils import set_key_pair
import os

class SignalTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(SignalTest, cls).setUpClass()
        set_key_pair()

    def make_request(self):
        request = Mock()
        request.session = {}
        return request

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.request = self.make_request()

    def test_remove_jwt_after_logout(self):
        user = self.user
        request = self.request

        jwt = make_login_token(user)
        token = jwt.token
        request.session['JWT'] = token

        user_logged_out.send(sender=user.__class__, request=request, user=user)

        with self.assertRaises(JWT.DoesNotExist):
            JWT.objects.get_model_from_token(token)

        self.assertNotIn('JWT', request.session)
