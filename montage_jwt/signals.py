from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .util import make_claims
from .models import JWT

@receiver(user_logged_in)
def add_jwt(sender, user, request, **kwargs):
    claims = make_claims(user, 'LOG')
    jwt = JWT.objects.create_token_from_claims(claims, user)
    request.session['JWT'] = jwt.token

@receiver(user_logged_out)
def remove_jwt(sender, user, request, **kwargs):
    token = request.session['JWT']
    jwt = JWT.objects.get_model_from_token(token)
    jwt.delete()
    del request.session['JWT']
