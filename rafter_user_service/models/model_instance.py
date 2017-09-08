from django.db import models
from .investigator import Investigator
from .investigation import Investigation
from .model_status import ModelStatus


class ModelInstance(models.Model):

    input_list = models.FileField(max_length=100)
    output_list = models.FileField(max_length=100)
    parameter_list = models.FileField(max_length=100)
    run_duration = models.IntegerField
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    model_status = models.ForeignKey(ModelStatus, related_name='%(class)s_model_status')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
