from django.test import TestCase
from rafter_user_service.models import Application
from django.contrib.auth.models import User
from django.urls import reverse
from .util import make_user, make_test_user, make_app

class ApplicationListViewTest(TestCase):
    def setUp(self):
        self.user = make_test_user()

    def get_apps(self):
        return self.client.get(reverse('user:apps'))

    def test_show_all_no_apps(self):
        response = self.get_apps()
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_show_all_one_app(self):
        make_app(self.user, name='test1')
        
        response = self.get_apps()
        self.assertQuerysetEqual(response.context['object_list'], ['<Application: test1>'])

    def test_show_all_two_apps(self):
        make_app(self.user, 'test1')
        make_app(self.user, 'test2')
        
        response = self.get_apps()
        # The order of this queryset is determined by Application.Meta.ordering
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<Application: test1>', '<Application: test2>']
        )

class ApplicationDetailViewTest(TestCase):
    def setUp(self):
        self.user = make_test_user()

    def test_show_app(self):
        app = make_app(self.user, 'test')
        response = self.client.get(reverse('user:detail_app', args=[app.pk]))
        self.assertContains(response, 'test')

    def test_show_app_login(self):
        app = make_app(self.user, 'test')
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('user:detail_app', args=[app.pk]))
        self.assertContains(response, 'Authenticate')

class ApplicationGetSecretTest(TestCase):
    def setUp(self):
        self.user = make_test_user()
        self.app = make_app(self.user, 'test')

    def get_secret(self, pk):
        return self.client.get(reverse('user:secret', args=[pk]))
        
    def test_get_app_no_app(self):
        response = self.get_secret(self.app.pk + 1)
        self.assertEqual(response.status_code, 404)

    def test_get_app_wrong_user(self):
        user_2 = make_user('test2')
        self.client.login(username='test2', password='test')
        response = self.get_secret(self.app.pk)

        self.assertEqual(response.status_code, 403)

    def test_get_app_correct_user(self):
        self.client.login(username='test', password='test')
        response = self.get_secret(self.app.pk)

        # Retrieve new app object since we altered the database.
        app = Application.objects.get(pk=self.app.pk)
        self.assertEqual(response.status_code, 200)
        secret_json = response.json()
        self.assertEqual(secret_json['app_id'], str(app.pk))
        self.assertTrue(app.check_token(secret_json['app_secret']))

class ApplicationAuthenticateTest(TestCase):
    def setUp(self):
        self.user = make_test_user()
        self.app = make_app(self.user, 'test')
        self.secret = self.app.generate_access_token()

    def get_auth(self, pk):
        return self.client.get(reverse('user:auth_app', args=[pk]))

    def post_auth(self, pk, **data):
        return self.client.post(reverse('user:auth_app', args=[pk]), data)

    def test_get_auth_no_user(self):
        response = self.get_auth(self.app.pk)
        self.assertEqual(response.status_code, 401)

    def test_post_auth_no_user_correct_secret(self):
        response = self.post_auth(self.app.pk, secret=self.secret)
        self.assertEqual(response.status_code, 200)

    def test_get_auth_wrong_user(self):
        user_2 = make_user('test2')
        self.client.login(username='test2', password='test')
        response = self.get_auth(self.app.pk)
        self.assertEqual(response.status_code, 403)

    def test_post_auth_wrong_user_correct_secret(self):
        user_2 = make_user('test2')
        self.client.login(username='test2', password='test')
        response = self.post_auth(self.app.pk, secret=self.secret)
        self.assertEqual(response.status_code, 200)

    def test_get_auth_correct_user(self):
        self.client.login(username='test', password='test')
        response = self.get_auth(self.app.pk)
        self.assertEqual(response.status_code, 200)

    def test_post_auth_correct_user_correct_secret(self):
        self.client.login(username='test', password='test')
        response = self.post_auth(self.app.pk, secret=self.secret)
        self.assertEqual(response.status_code, 200)
