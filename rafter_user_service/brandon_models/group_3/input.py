from django.db import models
from ..investigator import Investigator

import datetime


class Input(models.Model):

    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)  # TODO check if this is correct
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator)
    modified_by = models.ForeignKey(Investigator)
    created_on = models.DateField(default=datetime.date.today)
    last_modified = models.DateField(default=datetime.date.today)
