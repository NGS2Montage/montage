from django.db import models
from .input import Input
from .output import Output
from .parameter import Parameter
from .investigator import Investigator


class Analysis(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    input = models.ManyToManyField(Input)
    output = models.ManyToManyField(Output)
    parameter = models.ManyToManyField(Parameter)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
