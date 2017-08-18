from django.db import models
from django.contrib.auth.models import User
from .settings import api_settings
import datetime
import uuid
import jwt

class JWTManager(models.Manager):
    def create_token_from_claims(self, claims, user=None):
        token = jwt.encode(claims, api_settings.PRIVATE_KEY, algorithm='RS512').decode('utf-8')

        if user is None:
            username = claims['sub']
            user = User.objects.get(username=username)

        return self.create(
            jwi=claims['jwi'], 
            token=token,
            scope=claims['scope'], 
            user=user
        )

    def get_model_from_token(self, token):
        jwi = JWT.get_jwi(token)
        return self.get(pk=jwi)

# Create your models here.
class JWT(models.Model):
    objects = JWTManager()

    jwi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.TextField()
    scope = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    revoked = models.BooleanField(default=False)

    def get_claims(self):
        return self.decode(self.token)
    
    def refresh(self):
        claims = self.get_claims()

        new_claims = {
            'jwi': str(uuid.uuid4()),
            'exp': datetime.utcfromtimestamp(claims['exp']) + get_exp_delta(claims['scope']),
            'orig_iat': claims['iat'],
            'iat': datetime.utcnow(),
        }

        claims.update(new_claims)
        return self.objects.create_token_from_claims(claims, user=self.user)

    def is_expired(self):
        claims = self.get_claims()
        exp = datetime.utcfromtimestamp(claims['exp'])
        now = datetime.utcnow()
        return now > exp

    def is_about_to_expire(self):
        claims = self.get_claims()
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
