from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from jwt import decode
from montage_jwt.models import JWT
from montage_jwt.util import make_claims

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

    def test_get_jwt_no_login(self):
        resp = self.client.get(reverse('montage_jwt:get_jwt', args=['api']))
        self.assertEqual(403, resp.status_code)

    def test_get_jwt_no_type(self):
        self.client.login(username='test', password='test')
        resp = self.client.get(reverse('montage_jwt:get_jwt', args=['non']))
        self.assertEqual(404, resp.status_code)

class RefreshJwtViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='test')
        
        claims = make_claims(self.user, 'API') 
        self.jwt = JWT.objects.create_token(claims, self.user)

    def test_refresh(self):
        token = self.jwt.token
        data = {
            'token': token,
        }
        resp = self.client.post(reverse('montage_jwt:refresh_jwt'), data)
        json = resp.json()

        self.assertEqual(200, resp.status_code)
        self.assertIn('token', json)

        token = json['token']
        claims = decode(token, verify=False)
        self.assertEqual(self.user.get_username(), claims['sub'])

    def test_refresh_no_token(self):
        data = {}
        resp = self.client.post(reverse('montage_jwt:refresh_jwt'), data)
        json = resp.json()

        self.assertEqual(400, resp.status_code)
