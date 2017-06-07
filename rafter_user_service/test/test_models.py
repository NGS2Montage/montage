from django.test import TestCase
from rafter_user_service.models import Application
from django.contrib.auth.models import User
from .util import make_user, make_test_user, make_app


class ProfileTest(TestCase):
    def test_make_user_makes_profile(self):
        user = make_test_user()
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.profile._roles, '[]')
        self.assertEqual(user.profile._access, '["@core", "#public"]')

    def test_roles(self):
        user = make_test_user()
        user.profile.roles = ['some', 'roles']
        self.assertEqual(user.profile._roles, '["some", "roles"]')
        self.assertEqual(user.profile.roles, ['some', 'roles'])

    def test_access(self):
        user = make_test_user()
        user.profile.access = ['some', 'access']
        self.assertEqual(user.profile._access, '["some", "access"]')
        self.assertEqual(user.profile.access, ['some', 'access'])

class ApplicationTest(TestCase):
    def setUp(self):
        self.user = make_test_user()
        
    def test_user(self):
        Application.objects.create(user=self.user, name='test')

    def test_user_user_is_none(self):
        with self.assertRaises(TypeError):
            Application.objects.create(user=None, name='test')

    def test_user_user_is_str(self):
        with self.assertRaises(TypeError):
            Application.objects.create(user='oh no!', name='test')

    def test_generate_access_token(self):
        app = make_app(self.user, 'test')
        token = app.generate_secret()

        self.assertIsNotNone(app.access_token)
        self.assertNotEqual(len(app.access_token), 0)
        self.assertTrue(app.check_secret(token))
