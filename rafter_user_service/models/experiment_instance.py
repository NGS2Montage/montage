from django.db import models
from .investigator import Investigator
from .experiment import Experiment
from .treatment import Treatment
from .experiment_status import ExperimentStatus
from .investigation import Investigation


class ExperimentInstance(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    experiment = models.ForeignKey(Experiment, related_name='%(class)s_experiment')
    treatment = models.ForeignKey(Treatment, related_name='%(class)s_treatment')
    experiment_status = models.ForeignKey(ExperimentStatus, related_name='%(class)s_experiment_status')
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
