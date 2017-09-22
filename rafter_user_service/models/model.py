from django.db import models

from .abstract import AuditedTimeStampedModel

from .theory import Theory
from .input import Input
from .output import Output
from .parameter import Parameter


class Model(AuditedTimeStampedModel):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    literature_reference = models.CharField(max_length=200)
    inputs = models.ManyToManyField(Input)
    outputs = models.ManyToManyField(Output)
    parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        return self.name
