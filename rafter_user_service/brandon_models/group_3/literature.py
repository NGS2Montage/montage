from django.db import models
from .theory import Theory
from .experiment import Experiment
from .model import Model
from ..investigator import Investigator

import datetime


class Literature(models.Model):
    ACTIVE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    theory = models.ManyToManyField(Theory)
    experiment = models.ManyToManyField(Experiment)
    model = models.ManyToManyField(Model)
    reference = models.CharField(max_length=200)
    bibtex = models.CharField(max_length=200)  # TODO is this spelling correct?
    is_active = models.CharField(choices=ACTIVE_CHOICES, default='N')
    created_by = models.ForeignKey(Investigator)
    modified_by = models.ForeignKey(Investigator)
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
