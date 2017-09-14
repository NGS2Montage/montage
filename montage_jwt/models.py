from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .settings import api_settings
from datetime import datetime
import uuid
import jwt

class ExpiredQuerySet(models.QuerySet):
    def expired(self):
        return self.filter(exp__lt=timezone.now())

class JWTManager(models.Manager):
    def create_token(self, claims, user=None):
        exp = claims['exp']
        token = jwt.encode(claims, api_settings.PRIVATE_KEY, algorithm=api_settings.ALGORITHM).decode('utf-8')

        username = claims['sub']
        if user is None:
            user = User.objects.get(username=username)
        elif user.get_username() != username:
            raise ValueError("user must be the same user as passed in claims['sub'].")

        return self.create(
            jwi=uuid.UUID(claims['jwi']), 
            token=token,
            scope=claims['scope'], 
            user=user,
            exp=exp,
        )

    def get_model_from_token(self, token):
        claims = jwt.decode(token, verify=False)
        return self.get(pk=claims['jwi'])

    def get_from_claims(self, claims):
        return self.get(pk=claims['jwi'])

# Create your models here.
class JWT(models.Model):
    objects = JWTManager()
    expired = ExpiredQuerySet.as_manager()

    jwi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.TextField(editable=False)
    scope = models.CharField(max_length=3, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    exp = models.DateTimeField(editable=False)

    # Only editable field.
    revoked = models.BooleanField(default=False)
