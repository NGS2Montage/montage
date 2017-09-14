from django.db import models
from .theory import Theory
from .experiment import Experiment
from .model import Model
from .investigator import Investigator


class Literature(models.Model):

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    theory = models.ManyToManyField(Theory)
    experiment = models.ManyToManyField(Experiment)
    model = models.ManyToManyField(Model)
    reference = models.CharField(max_length=200)
    bibtex = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
