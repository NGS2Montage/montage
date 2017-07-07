from django.db import models
from .manipulation import Manipulation
from .population import Population
from ..investigator import Investigator

import datetime


class Treatment(models.Model):

    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    manipulation = models.ManyToManyField(Manipulation)
    population = models.ManyToManyField(Population)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator)
    modified_by = models.ForeignKey(Investigator)
    created_on = models.DateField(default=datetime.date.today)
    last_modified = models.DateField(default=datetime.date.today)
