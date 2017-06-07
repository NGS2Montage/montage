from django.test import TestCase
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from importlib import import_module
from .util import make_test_user

class AddJWTTest(TestCase):
    
    def test_add_jwt(self):
        user = make_test_user()
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore(None)
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        self.assertIn('JWT', request.session)
