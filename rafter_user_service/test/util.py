from django.contrib.auth.models import User

def make_user(username):
    return User.objects.create_user(username, 'test@test.com', 'test')

def make_test_user():
    return make_user('test')
