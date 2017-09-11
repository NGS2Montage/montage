from django.db import models

from .abstract import AuditedTimeStampedModel


class ProjectState(AuditedTimeStampedModel):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
