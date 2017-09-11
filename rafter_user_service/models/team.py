from django.db import models

from .abstract import AuditedTimeStampedModel


class Team(AuditedTimeStampedModel):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
