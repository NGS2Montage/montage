from django.db import models

from .abstract import AuditedTimeStampedModel
from .project_state import ProjectState
from .team import Team


class Project(AuditedTimeStampedModel):

    description = models.CharField(max_length=200)
    team = models.ForeignKey(Team, related_name='%(class)s_team')
    project_state = models.ForeignKey(ProjectState, related_name='%(class)s_project_state')

    def __str__(self):
        return '({}) {}'.format(self.team, self.description)
