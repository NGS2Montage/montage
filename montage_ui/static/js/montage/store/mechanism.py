from django.db import models

from .abstract import AuditedTimeStampedModel


class Mechanism(AuditedTimeStampedModel):

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
