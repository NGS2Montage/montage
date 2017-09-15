from django.db import models

from .abstract import AuditedTimeStampedModel
from .project import Project
from .investigator import Investigator
from .investigation_status import InvestigationStatus



class Investigation(AuditedTimeStampedModel):

    project = models.ForeignKey(Project, related_name='%(class)s_project')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    investigation_status = models.ForeignKey(InvestigationStatus, related_name='%(class)s_investigation_status')
