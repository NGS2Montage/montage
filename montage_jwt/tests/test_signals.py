from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.http.request import HttpRequest
from django.conf import settings
from importlib import import_module
from montage_jwt.settings import api_settings
from montage_jwt.models import Token
import jwt
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
        request = HttpRequest()
        request.session = self.engine.SessionStore(None)
        return request

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.engine = import_module(settings.SESSION_ENGINE)
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
        claims = jwt.decode(token, verify=False)
        jwi = claims['jwi']
        token = Token.objects.get(pk=jwi)

    def test_remove_jwt_after_logout(self):
        user = self.user
        request = self.request
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIn('JWT', request.session)

        token = request.session['JWT']
        claims = jwt.decode(token, verify=False)
        jwi = claims['jwi']

        user_logged_out.send(sender=user.__class__, request=request, user=user)

        with self.assertRaises(Token.DoesNotExist):
            Token.objects.get(pk=jwi)

        self.assertNotIn('JWT', request.session)
