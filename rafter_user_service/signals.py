from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def add_jwt(sender, user, request, **kwargs):
    token = user.profile.generate_token()
    request.session['JWT'] = token
