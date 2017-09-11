from django.db import models
from .investigator import Investigator
from .investigation import Investigation
from .analysis import Analysis


class ConfirmatoryLoop(models.Model):

    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    analysis = models.ForeignKey(Analysis, related_name='%(class)s_analysis')
    # TODO "(Model Validation -- what form should this be -- how does this generate the “next” loop?)"
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
