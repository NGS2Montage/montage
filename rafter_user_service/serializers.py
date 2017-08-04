from rest_framework import serializers
from rafter_user_service.models import *
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class ApplicationJWTSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    secret = serializers.CharField(write_only=True)

    def validate(self, data):
        app = self.context['app']
        
        if not app.check_secret(data['secret']):
            msg = 'Wrong application secret.'
            raise serializers.ValidationError(msg)

        return {
            'token': app.profile.generate_token()
        }


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'desc')


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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'team', 'project_state')


class ProjectStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectState
        fields = ('id', 'name')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
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
