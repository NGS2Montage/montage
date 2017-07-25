from django.db import models
from .investigator import Investigator
from .investigation import Investigation


class AnalysisInstance(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    # TODO begin -> These fields have a non-relational concern. Need to discuss
    input_list = models.CharField(max_length=200)
    output_list = models.CharField(max_length=200)
    parameter_list = models.CharField(max_length=200)
    # TODO end
    run_duration = models.IntegerField
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
