from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import ProjectState, Investigator, Observation, Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Observation)
class ObservationAdmin(SimpleHistoryAdmin):
    pass

@admin.register(Investigator)
class InvestigatorAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectState)
class ProjectStateAdmin(admin.ModelAdmin):
    pass
