from django.db import models
from .team import Team
from .project_state import ProjectState
from .investigator import Investigator


class Project(models.Model):

    rid = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    team = models.ForeignKey(Team, related_name='%(class)s_team')
    project_state = models.ForeignKey(ProjectState, related_name='%(class)s_project_state')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
