from django.db import models
from .input import Input
from .output import Output
from .parameter import Parameter

import datetime


class Analysis(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    input = models.ManyToManyField(Input)
    output = models.ManyToManyField(Output)
    parameter = models.ManyToManyField(Parameter)
    is_active = models.CharField(max_length=200)  # TODO
    created_by = models.ForeignKey('rafter_user_service.investigator')
    modified_by = models.ForeignKey('rafter_user_service.investigator')
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
