from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.signals import request_started
from django.dispatch import receiver
from .util import make_token
from .models import Token
import jwt

@receiver(user_logged_in)
def add_jwt(sender, user, request, **kwargs):
    token = make_token(user, 'LOG')
    token = token.token
    request.session['JWT'] = token

@receiver(user_logged_out)
def remove_jwt(sender, user, request, **kwargs):
    token = request.session['JWT']
    claims = jwt.decode(token, verify=False)
    jwi = claims['jwi']
    token = Token.objects.get(pk=jwi)
    token.delete()
    del request.session['JWT']
