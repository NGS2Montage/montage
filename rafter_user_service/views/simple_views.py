from rest_framework import viewsets

from rafter_user_service import models, serializers


class ProjectStateViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProjectStateSerializer
    queryset = models.ProjectState.objects.all()


class TeamViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()


class ExperimentViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ExperimentSerializer
    queryset = models.Experiment.objects.all()


class AnalysisViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AnalysisSerializer
    queryset = models.Analysis.objects.all()


class HypothesisViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.HypothesisSerializer
    queryset = models.Hypothesis.objects.all()


class TheoryViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.TheorySerializer
    queryset = models.Theory.objects.all()


class MechanismViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.MechanismSerializer
    queryset = models.Mechanism.objects.all()
