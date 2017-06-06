from django.contrib.auth.models import User
from rafter_user_service.models import Application

def make_user(username):
    return User.objects.create_user(username, 'test@test.com', 'test')

def make_test_user():
    return make_user('test')

def make_app(user, name):
    return Application.objects.create(user=user, name=name) 
