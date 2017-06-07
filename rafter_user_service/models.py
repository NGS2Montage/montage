from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from rest_framework_jwt.settings import api_settings
import bcrypt
import string
import random
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
        return jwt_encode_handler(payload)
        
    def __str__(self):
        return self.user.username

class Application(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.TextField(max_length=80)
    desc = models.TextField(max_length=200, blank=True)
    access_token = models.BinaryField(max_length=100, blank=True)

    class Meta:
        ordering = ["name"]

    @property
    def user(self):
        return self.profile.user

    @user.setter
    def user(self, value):
        self.profile = value.profile

    def generate_secret(self):
        charset = string.ascii_uppercase + string.digits + string.ascii_lowercase
        token = ''.join(random.choices(charset, k=30))

        # Hash the token for storage
        hashed = bcrypt.hashpw(token.encode('utf-8'), bcrypt.gensalt())
        self.access_token = hashed 

        # Return the unhashed token
        return token

    def check_secret(self, token):
        return self.access_token and bcrypt.hashpw(token.encode('utf-8'), self.access_token) == self.access_token

    def __str__(self):
        return self.name

