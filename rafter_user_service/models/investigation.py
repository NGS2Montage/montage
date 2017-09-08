from django.db import models
from .project import Project
from .investigator import Investigator
from .investigation_status import InvestigationStatus


class Investigation(models.Model):

    project = models.ForeignKey(Project, related_name='%(class)s_project')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    investigation_status = models.ForeignKey(InvestigationStatus, related_name='%(class)s_investigation_status')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
