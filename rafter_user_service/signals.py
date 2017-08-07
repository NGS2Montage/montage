from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def add_jwt(sender, user, request, **kwargs):
    profile = user.profile
    profile.token = profile.generate_token()

@receiver(user_logged_out)
def remove_jwt(sender, user, request, **kwargs):
    user.profile.delete_token()
