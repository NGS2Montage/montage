from django.db import models
from .theory import Theory
from .input import Input
from .output import Output
from .parameter import Parameter

import datetime


class Model(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    literature_reference = models.CharField(max_length=200)
    theory = models.ManyToManyField(Theory)
    input = models.ManyToManyField(Input)
    output = models.ManyToManyField(Output)
    parameter = models.ManyToManyField(Parameter)
    created_by = models.ForeignKey('rafter_user_service.investigator')
    modified_by = models.ForeignKey('rafter_user_service.investigator')
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
