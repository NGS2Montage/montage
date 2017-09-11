from django.conf import settings
from django.db import models

from .abstract import AuditedTimeStampedModel
from .project import Project


class Observation(AuditedTimeStampedModel):
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(Project, related_name='%(class)s_project')

    def __str__(self):
        return '({}) {}'.format(self.created_by.username, self.comment)
