from django.db import models
from .investigator import Investigator


class Input(models.Model):

    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)  # TODO check if this is correct
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(Investigator, related_name='%(class)s_creator')
    modified_by = models.ForeignKey(Investigator, related_name='%(class)s_last_modifier')
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)