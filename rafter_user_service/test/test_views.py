from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .util import make_user, make_test_user

class UserDetailViewTest(TestCase):
    def setUp(self):
        self.user = make_test_user()

    def get_user(self):
        return self.client.get(reverse('user:user', args=[self.user.username]))

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = make_test_user()

    def test_show_user_no_login(self):
        response = self.client.get(reverse('user:profile'))
        self.assertRedirects(
            response,
            reverse('auth_login') + '?next=/user/', 
            status_code=302, 
            target_status_code=200
        )

    def test_show_user_with_login(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('user:profile'))
        self.assertRedirects(
            response,
            reverse('user:user', args=[self.user.username]), 
            status_code=301, 
            target_status_code=200
        )
