from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from .models import JWT

@receiver(user_logged_out)
def remove_jwt(sender, user, request, **kwargs):
    token = request.session['JWT']
    jwt = JWT.objects.get_model_from_token(token)
    jwt.delete()
    del request.session['JWT']
