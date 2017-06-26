from django.contrib.auth.models import User
from django.db import models

import datetime


class Role(models.Model):
    ACTIVE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    role = models.CharField(max_length=200, unique=True)  # TODO probably should be unique
    user = models.ForeignKey(User)
    is_active = models.CharField(choices=ACTIVE_CHOICES, default='N')
    created_by = models.CharField(max_length=200, unique=True)
    modified_by = models.CharField(max_length=200, unique=True)
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
