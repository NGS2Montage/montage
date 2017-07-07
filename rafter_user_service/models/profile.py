from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from rest_framework_jwt.settings import api_settings
import json

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Only including fields that are used in the JWT
    _roles = models.TextField(max_length=200, default='[]')
    _access = models.TextField(max_length=200, default='["@core", "#public"]')

    # Hack below since we can't store lists in the database.  Note, with this
    # implementation doing something like self.roles.append(...) will not be
    # possible.
    @property
    def roles(self):
        return json.loads(self._roles)

    @roles.setter
    def roles(self, value):
        self._roles = json.dumps(value)

    @property
    def access(self):
        return json.loads(self._access)

    @access.setter
    def access(self, value):
        self._access = json.dumps(value)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def generate_token(self):
        payload = jwt_payload_handler(self.user)
        payload['aud'] = self.access
        payload['roles'] = self.roles
        payload['sub'] = payload['username']
        del payload['username']
        now = datetime.utcnow()
        payload['iat'] = now
        payload['nbf'] = now

        jwt = jwt_encode_handler(payload)
        return jwt

    def __str__(self):
        return self.user.username
