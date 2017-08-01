from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from rest_framework_jwt.settings import api_settings
import jwt
import json

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _token = models.TextField(max_length=200, null=True)

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

    @property
    def token(self):
        '''Raises an exception if the decode fails.  This is so we can fail if
        the token has expired.  Token should only be set using generate_token.
        '''

        if self._token is None:
            return None

        now = datetime.utcnow()

        # Always trust this token because it should only be set with
        # generate_token, might be a bit smelly
        claims = jwt.decode(self._token, verify=False)
        nbf = claims['nbf']
        exp = claims['exp'] 

        nbf = datetime.utcfromtimestamp(nbf)
        exp = datetime.utcfromtimestamp(exp)

        if now > exp:
            raise jwt.exceptions.ExpiredSignatureError

        if nbf > now:
            raise jwt.exceptions.ImmatureSignatureError

        # getter returns tuple, setter will only take the token
        return self._token, claims

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

        self._token = jwt
        return jwt

    def delete_token(self):
        self._token = None

    def __str__(self):
        return self.user.username
