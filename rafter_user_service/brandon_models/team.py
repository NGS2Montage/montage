from django.db import models

import datetime


class Team(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    # is_active = TODO figure this out
    created_by = models.CharField(max_length=200, unique=True)
    modified_by = models.CharField(max_length=200, unique=True)
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
