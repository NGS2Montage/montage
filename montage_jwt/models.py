from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.
class Token(models.Model):

    jwi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.TextField()
    scope = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    revoked = models.BooleanField(default=False)
