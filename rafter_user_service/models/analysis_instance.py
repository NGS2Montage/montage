from django.db import models
from .investigator import Investigator
from .investigation import Investigation


class AnalysisInstance(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    run_duration = models.IntegerField
    # TODO add Analysis status
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
