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


class ConfirmatoryLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfirmatoryLoop


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiment


class ExperimentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperimentInstance


class ExperimentStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalysisInstance


class ExperimentLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExploratoryLoop


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input


class InvestigationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investigation


class InvestigationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvestigationStatus


class InvestigatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investigator


class LiteratureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Literature


class ManipulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manipulation


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model


class ModelInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelInstance


class ModelStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelStatus


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Output


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Population


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project


class ProjectStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectState


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team


class TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theory


class TheoryInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TheoryInstance


class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Treatment
