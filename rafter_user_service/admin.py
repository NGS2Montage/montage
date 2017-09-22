from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from . import models


@admin.register(models.Analysis)
class AnalysisAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Input)
class InputAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Output)
class OutputAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Parameter)
class ParameterAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Model)
class ModelAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Hypothesis)
class HypothesisAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Experiment)
class ExperimentAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Mechanism)
class MechanismAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Investigator)
class InvestigatorAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.Investigation)
class InvestigationAdmin(SimpleHistoryAdmin):
    pass


@admin.register(models.InvestigationStatus)
class InvestigationStatusAdmin(SimpleHistoryAdmin):
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


@admin.register(models.Theory)
class TheoryAdmin(SimpleHistoryAdmin):
    pass