from django.db import models
from ..investigator import Investigator

import datetime


class InvestigationStatus(models.Model):
    ACTIVE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_active = models.CharField(choices=ACTIVE_CHOICES, default='N')
    created_by = models.ForeignKey(Investigator)
    modified_by = models.ForeignKey(Investigator)
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
