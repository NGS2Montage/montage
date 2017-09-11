from django.db import models
from .manipulation import Manipulation
from .population import Population
from .investigator import Investigator


class Treatment(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    manipulation = models.ManyToManyField(Manipulation)
    population = models.ManyToManyField(Population)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
