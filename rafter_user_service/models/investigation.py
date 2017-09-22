from django.db import models

from .abstract import AuditedTimeStampedModel
from .project import Project
from .experiment import Experiment
from .hypothesis import Hypothesis
from .model import Model
from .investigation_status import InvestigationStatus
from .mechanism import Mechanism
from .theory import Theory


class Investigation(AuditedTimeStampedModel):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    experiments = models.ManyToManyField(Experiment, blank=True, related_name='%(class)s_experiment')
    hypotheses = models.ManyToManyField(Hypothesis, blank=True, related_name='%(class)s_hypothesis')
    investigation_status = models.ForeignKey(InvestigationStatus, related_name='%(class)s_investigation_status')
    mechanisms = models.ManyToManyField(Mechanism, blank=True, related_name='%(class)s_mechanism')
    theories = models.ManyToManyField(Theory, blank=True, related_name='%(class)s_theory')
    models = models.ManyToManyField(Model, blank=True, related_name='%(class)s_model')

    def __str__(self):
        return self.name
