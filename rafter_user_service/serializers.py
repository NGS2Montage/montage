from rest_framework import serializers
from rafter_user_service.models import *
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id', 'name')


class AnalysisInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalysisInstance
        fields = 'id'


class ConfirmatoryLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfirmatoryLoop
        fields = 'id'


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiment
        fields = ('id', 'name')


class ExperimentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperimentInstance
        fields = ('id', 'experiment', 'experiment_status')


class ExperimentStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperimentStatus
        fields = ('id', 'name')


class ExperimentLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExploratoryLoop
        fields = 'id'


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ('id', 'name')


class InvestigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investigation
        fields = ('id', 'name', 'project')


class InvestigationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvestigationStatus
        fields = ('id', 'name')


class InvestigatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investigator
        fields = ('id', 'name', 'user_name')


class LiteratureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Literature
        fields = ('id', 'name', 'author')


class ManipulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manipulation
        fields = ('id', 'name')


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'name')


class ModelInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelInstance
        fields = 'id'


class ModelStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelStatus
        fields = ('id', 'name')


class ObservationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    modified_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Observation
        fields = ('comment', 'project', 'date_created', 'last_modified', 'created_by', 'modified_by')
        read_only_fields = ('date_created', 'last_modified')


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Output
        fields = ('id', 'name','type')


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        fields = ('id', 'name','type')


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Population
        fields = ('id', 'name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user')


class ProjectStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectState
        fields = ('id', 'name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    modified_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    project_state = ProjectStateSerializer()
    team = TeamSerializer()

    class Meta:
        model = Project
        fields = ('id', 'description', 'team', 'project_state', 'created_by', 'modified_by', 'date_created', 'last_modified')
        read_only_fields = ('project_state', 'created_by', 'modified_by', 'date_created', 'last_modified')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theory
        fields = ('id', 'name')


class TheoryInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TheoryInstance
        fields = ('id', 'name', 'model')


class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Treatment
        fields = ('id', 'name')
