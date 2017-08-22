from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .settings import api_settings
from .util import get_exp_delta
from datetime import datetime
import uuid
import jwt

class ExpiredQuerySet(models.QuerySet):
    def expired(self):
        return self.filter(exp__lt=timezone.now())

class JWTManager(models.Manager):
    def create_token_from_claims(self, claims, user=None):
        exp = claims['exp']
        token = jwt.encode(claims, api_settings.PRIVATE_KEY, algorithm='RS512').decode('utf-8')

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
        jwi = JWT.get_jwi(token)
        return self.get(pk=jwi)

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

    def get_claims(self):
        return self.decode(self.token)
    
    def refresh(self):
        claims = self.get_claims()

        new_claims = {
            'jwi': str(uuid.uuid4()),
            'exp': timezone.make_aware(datetime.utcfromtimestamp(claims['exp']) + get_exp_delta(claims['scope'])),
            'orig_iat': claims['iat'],
            'iat': timezone.now(),
        }

        claims.update(new_claims)
        return JWT.objects.create_token_from_claims(claims, user=self.user)

    def is_expired(self):
        exp = self.exp
        now = datetime.utcnow()
        return now > exp

    def is_about_to_expire(self):
        exp = self.exp
        now = datetime.utcnow()
        return now > exp - api_settings.REFRESH_THRESHOLD 

    # These next two methods are useful because they can be used on tokens
    # without having to do a database operation.
    @staticmethod
    def is_token_expired(token):
        claims = JWT.decode(token)
        exp = datetime.utcfromtimestamp(claims['exp'])
        now = datetime.utcnow()
        return now > exp

    @staticmethod
    def is_token_about_to_expire(token):
        claims = JWT.decode(token)
        exp = datetime.utcfromtimestamp(claims['exp'])
        now = datetime.utcnow()
        return now > exp - api_settings.REFRESH_THRESHOLD 
    
    @staticmethod
    def get_jwi(token):
        claims = jwt.decode(token, verify=False)
        return claims['jwi']
    
    @staticmethod
    def decode(token):
        return jwt.decode(token, verify=False)
