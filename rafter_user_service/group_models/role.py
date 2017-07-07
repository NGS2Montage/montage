from django.contrib.auth.models import User
from django.db import models

import datetime


class Role(models.Model):

    role = models.CharField(max_length=200, unique=True)  # TODO probably should be unique
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=200, unique=True)
    modified_by = models.CharField(max_length=200, unique=True)
    created_on = models.DateField(default=datetime.date.today)
    last_modified = models.DateField(default=datetime.date.today)
