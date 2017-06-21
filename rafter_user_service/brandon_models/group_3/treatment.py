from django.db import models

import datetime


class Treatment(models.Model):
    created_by = models.ForeignKey('rafter_user_service.investigator')
    modified_by = models.ForeignKey('rafter_user_service.investigator')
    created_on = models.CharField(datetime.date.today())
    last_modified = models.CharField(datetime.date.today())
