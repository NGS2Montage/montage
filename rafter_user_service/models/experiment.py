from django.db import models

from .abstract import AuditedTimeStampedModel
from .project import Project

# from .manipulation import Manipulation
# from .population import Population
# from .treatment import Treatment


class Experiment(AuditedTimeStampedModel):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # manipulation = models.ManyToManyField(Manipulation)
    # population = models.ManyToManyField(Population)
    # treatment = models.ManyToManyField(Treatment)
    method = models.CharField(max_length=200)
    protocol = models.FileField(max_length=200, blank=True)
    consent = models.FileField(max_length=200, blank=True)
    recruitment = models.FileField(max_length=200, blank=True)

    def __str__(self):
        return self.name
