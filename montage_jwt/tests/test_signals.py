from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from montage_jwt.settings import api_settings
from montage_jwt.models import JWT
from unittest.mock import Mock
import os

class SignalTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(SignalTest, cls).setUpClass()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        p_key_file = dir_path + '/private.pem'

        with open(p_key_file, 'r') as f:
            p_key = f.read().strip()

        api_settings.PRIVATE_KEY = p_key

    def make_request(self):
        request = Mock()
        request.session = {}
        return request

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.request = self.make_request()

    def test_no_login_no_jwt(self):
        user = self.user
        request = self.request
        self.assertNotIn('JWT', request.session)

    def test_add_jwt_after_login(self):
        user = self.user
        request = self.request
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIn('JWT', request.session)

        token = request.session['JWT']
        jwt = JWT.objects.get_model_from_token(token)

    def test_remove_jwt_after_logout(self):
        user = self.user
        request = self.request
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIn('JWT', request.session)

        token = request.session['JWT']

        user_logged_out.send(sender=user.__class__, request=request, user=user)

        with self.assertRaises(JWT.DoesNotExist):
            JWT.objects.get_model_from_token(token)

        self.assertNotIn('JWT', request.session)
