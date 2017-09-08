from django.db import models
from .investigator import Investigator
from .investigation import Investigation
from .model import Model


class TheoryInstance(models.Model):

    investigation = models.ForeignKey(Investigation, related_name='%(class)s_investigation')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    model = models.ManyToManyField(Model, related_name='%(class)s_model')
    reference = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
