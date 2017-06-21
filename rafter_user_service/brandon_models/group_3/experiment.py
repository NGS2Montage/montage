from django.db import models
from .manipulation import Manipulation
from .population import Population
from .treatment import Treatment

import datetime


class Experiment(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    manipulation = models.ManyToManyField(Manipulation)
    population = models.ManyToManyField(Population)
    treatment = models.ManyToManyField(Treatment)
    method = models.CharField(max_length=200)
    protocol = models.CharField(max_length=200)  # TODO file type?
    consent = models.CharField(max_length=200)  # TODO file type?
    recruitment = models.CharField(max_length=200)  # TODO file type?
    created_by = models.ForeignKey('rafter_user_service.investigator')
    modified_by = models.ForeignKey('rafter_user_service.investigator')
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
