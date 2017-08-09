from django.test import TestCase
from django.contrib.auth.models import User
from ..util import make_test_user

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
