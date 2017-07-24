from django.db import models
from .investigator import Investigator
from .investigation import Investigation
from .model_status import ModelStatus


class ModelInstance(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    run_duration = models.IntegerField
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    model_status = models.ForeignKey(ModelStatus, related_name='%(class)s_model_status')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
