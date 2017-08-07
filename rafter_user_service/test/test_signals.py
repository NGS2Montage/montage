from django.test import TestCase
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from importlib import import_module
from .util import make_test_user

class AddJWTTest(TestCase):

    def test_no_login_no_jwt(self):
        user = make_test_user()
        request = HttpRequest()
        self.assertIsNone(user.profile.token)

    def test_add_jwt_after_login(self):
        user = make_test_user()
        request = HttpRequest()
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIsNotNone(user.profile.token)

    def test_no_jwt_after_logout(self):
        user = make_test_user()
        request = HttpRequest()
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIsNotNone(user.profile.token)
        user_logged_out.send(sender=user.__class__, request=request, user=user)
        self.assertIsNone(user.profile.token)
