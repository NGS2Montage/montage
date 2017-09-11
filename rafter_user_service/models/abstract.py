from django.conf import settings
from django.db import models

from simple_history.models import HistoricalRecords


class AuditedTimeStampedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by'
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_modified_by'
    )

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    # for simple_history modified_by
    @property
    def _history_user(self):
        return self.modified_by

    @_history_user.setter
    def _history_user(self, value):
        self.modified_by = value
