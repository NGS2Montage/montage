from django.db import models
from .manipulation import Manipulation
from .population import Population
from .treatment import Treatment
from .investigator import Investigator


class Experiment(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    manipulation = models.ManyToManyField(Manipulation)
    population = models.ManyToManyField(Population)
    treatment = models.ManyToManyField(Treatment)
    method = models.CharField(max_length=200)
    protocol = models.FileField(max_length=200)
    consent = models.FileField(max_length=200)
    recruitment = models.FileField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
