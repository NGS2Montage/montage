from django.db import models
from django.conf import settings
from .team import Team


class Investigator(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    team = models.ForeignKey(Team)
    affiliation = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    # created_by = models.ForeignKey(Investigator)
    # modified_by = models.ForeignKey(Investigator)
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
