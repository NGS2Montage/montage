from django.db import models

from .abstract import AuditedTimeStampedModel
from .investigation import Investigation


class Analysis(AuditedTimeStampedModel):

    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.text
