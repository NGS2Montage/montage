from django.db import models

import datetime


class Role(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200, unique=True)  # TODO probably should be unique
    user = models.ForeignKey('rafter_user_service.User')
    is_active = models.CharField(max_length=200)  # TODO review this
    created_by = models.CharField(max_length=200, unique=True)
    modified_by = models.CharField(max_length=200, unique=True)
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
