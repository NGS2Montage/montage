from django.db import models
from django.conf import settings


class Observation(models.Model):

    comment = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
