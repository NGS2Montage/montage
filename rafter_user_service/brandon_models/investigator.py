from django.db import models

import datetime


class Investigator(models.Model):
    rid = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey('rafter_user_service.User')
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # team model?
    affiliation = models.CharField(max_length=200)  # TODO come back to this may. Consult notes
    is_active = models.CharField(max_length=200)  # TODO also review this
    # createdBy ( investigator model )
    # modified ( investigator model )
    created_on = models.CharField(datetime.date.today())  # TODO this and below may need be different types
    last_modified = models.CharField(datetime.date.today())
