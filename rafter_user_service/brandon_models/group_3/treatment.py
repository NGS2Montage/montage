from django.db import models
from .manipulation import Manipulation
from .population import Population

import datetime


class Treatment(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    manipulation = models.ManyToManyField(Manipulation)
    population = models.ManyToManyField(Population)
    is_active = models.CharField(max_length=200)  # TODO
    created_by = models.ForeignKey('rafter_user_service.investigator')
    modified_by = models.ForeignKey('rafter_user_service.investigator')
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
