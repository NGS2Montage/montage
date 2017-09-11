from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from . import models


@admin.register(models.Investigator)
class InvestigatorAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Observation)
class ObservationAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Project)
class ProjectAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.ProjectState)
class ProjectStateAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Team)
class TeamAdmin(SimpleHistoryAdmin):
    list_display = ('name',)
