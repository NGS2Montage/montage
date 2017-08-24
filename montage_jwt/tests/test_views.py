from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from jwt import decode

class GetJwtViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='test')

    def test_get_jwt_user_logged_in(self):
        self.client.login(username='test', password='test')
        resp = self.client.get(reverse('montage_jwt:get_jwt', args=['api']))
        json = resp.json()

        self.assertEqual(200, resp.status_code)
        self.assertIn('token', json)

        token = json['token']
        claims = decode(token, verify=False)
        self.assertEqual(self.user.get_username(), claims['sub'])
