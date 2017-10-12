from rest_framework import serializers
from rafter_user_service import models
# from django.shortcuts import get_object_or_404
# from rest_framework.exceptions import PermissionDenied


class MyBaseSerializer(serializers.ModelSerializer):
    def get_fields(self):
        fields = super(MyBaseSerializer, self).get_fields()
        fields['id'] = serializers.IntegerField(label='ID', read_only=True)
        fields['created_by'] = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
        fields['modified_by'] = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
        fields['date_created'] = serializers.DateTimeField(read_only=True)
        fields['last_modified'] = serializers.DateTimeField(read_only=True)
        return fields


class ProjectStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectState
        fields = ('name', 'description')


class TeamSerializer(MyBaseSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    modified_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Team
        fields = ('name', 'description', 'location', 'website', 'affiliation', 'created_by', 'modified_by')


class ProjectSerializer(MyBaseSerializer):
    investigations = serializers.HyperlinkedRelatedField(
        source='investigation_set',
        many=True,
        view_name="api:investigation-detail",
        queryset=models.Investigation.objects.all()
    )

    class Meta:
        model = models.Project
        fields = ('name', 'description', 'team', 'project_state', 'investigations')

    def to_representation(self, instance):
        representation = super(ProjectSerializer, self).to_representation(instance)
        representation['team'] = TeamSerializer(instance.team).data
        representation['project_state'] = ProjectStateSerializer(instance.project_state).data
        return representation


class HypothesisSerializer(MyBaseSerializer):
    class Meta:
        model = models.Hypothesis
        fields = ('text',)


class MechanismSerializer(MyBaseSerializer):
    class Meta:
        model = models.Mechanism
        fields = ('text',)


class TheorySerializer(MyBaseSerializer):
    class Meta:
        model = models.Theory
        fields = ('text',)


class InvestigationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvestigationStatus
        fields = ('name', 'description')


class ModelSerializer(MyBaseSerializer):
    class Meta:
        model = models.Model
        fields = ('name', 'description', 'literature_reference', 'inputs', 'outputs', 'parameters')

    def to_representation(self, instance):
        representation = super(ModelSerializer, self).to_representation(instance)
        representation['inputs'] = InputSerializer(instance.inputs, many=True).data
        representation['outputs'] = OutputSerializer(instance.outputs, many=True).data
        representation['parameters'] = ParameterSerializer(instance.parameters, many=True).data
        return representation


class ExperimentSerializer(MyBaseSerializer):
    class Meta:
        model = models.Experiment
        fields = ('name', 'description', 'method', 'protocol', 'consent', 'recruitment')


class InvestigationSerializer(MyBaseSerializer):
    analysis = serializers.PrimaryKeyRelatedField(source='analysis_set', many=True, queryset=models.Analysis.objects.all())

    class Meta:
        model = models.Investigation
        fields = (
            'analysis',
            'experiments',
            'hypotheses',
            'investigation_status',
            'mechanisms',
            'models',
            'name',
            'project',
            'theories',
        )

    def to_representation(self, instance):
        representation = super(InvestigationSerializer, self).to_representation(instance)
        representation['analysis'] = AnalysisSerializer(instance.analysis_set, many=True).data
        representation['experiments'] = ExperimentSerializer(instance.experiments, many=True).data
        representation['hypotheses'] = HypothesisSerializer(instance.hypotheses, many=True).data
        representation['investigation_status'] = InvestigationStatusSerializer(instance.investigation_status).data
        representation['models'] = ModelSerializer(instance.models, many=True).data
        representation['mechanisms'] = MechanismSerializer(instance.mechanisms, many=True).data
        representation['theories'] = TheorySerializer(instance.theories, many=True).data
        return representation


class AnalysisSerializer(MyBaseSerializer):
    class Meta:
        model = models.Analysis
        fields = ('text', 'investigation')


class AnalysisInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AnalysisInstance
        fields = 'id'


class ConfirmatoryLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ConfirmatoryLoop
        fields = 'id'


class ExperimentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExperimentInstance
        fields = ('id', 'experiment', 'experiment_status')


class ExperimentStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExperimentStatus
        fields = ('id', 'name')


class ExperimentLoopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExploratoryLoop
        fields = 'id'


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Input
        fields = ('id', 'name', 'description', 'type')


class InvestigatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Investigator
        fields = ('id', 'name', 'user_name')


class LiteratureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Literature
        fields = ('id', 'name', 'author')


class ManipulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manipulation
        fields = ('id', 'name')


class ModelInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ModelInstance
        fields = 'id'


class ModelStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ModelStatus
        fields = ('id', 'name')


class ObservationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    modified_by = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Observation
        fields = ('comment', 'project', 'date_created', 'last_modified', 'created_by', 'modified_by')
        read_only_fields = ('date_created', 'last_modified')


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Output
        fields = ('id', 'name', 'description', 'type')


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Parameter
        fields = ('id', 'name', 'description', 'type')


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Population
        fields = ('id', 'name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('id', 'user')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ('id', 'name')


class TheoryInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TheoryInstance
        fields = ('id', 'name', 'model')


class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Treatment
        fields = ('id', 'name')
