from django.db import models
from .investigator import Investigator
from .investigation import Investigation


class AnalysisInstance(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    input_list = models.FileField(max_length=100)
    output_list = models.FileField(max_length=100)
    parameter_list = models.FileField(max_length=100)
    run_duration = models.IntegerField
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
