from django.contrib.auth.models import User
from django.db import models
from .team import Team

import datetime


class Investigator(models.Model):

    user = models.ForeignKey(User)
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    team = models.ForeignKey(Team.name)
    affiliation = models.CharField(max_length=200)  # TODO come back to this may. Consult notes
    is_active = models.BooleanField(default=False)
    # createdBy ( investigator model )
    # modified ( investigator model )
    created_on = models.CharField(default=datetime.date.today)
    last_modified = models.CharField(default=datetime.date.today)
