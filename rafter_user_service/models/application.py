from django.db import models
from rest_framework_jwt.settings import api_settings
from .profile import Profile
import bcrypt
import string
import random

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


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
