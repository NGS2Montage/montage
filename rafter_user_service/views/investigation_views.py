from rafter_user_service.models import Investigation
from rest_framework import viewsets
from rafter_user_service.serializers import InvestigationSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Analysis
from rest_framework.views import APIView


class InvestigationViewSet(viewsets.ModelViewSet):

    serializer_class = InvestigationSerializer
    queryset = Investigation.objects.all()

    def retrieve_investigation(self, pk=None):
        investigation = get_object_or_404(Investigation, id=pk)
        serializer = InvestigationSerializer(investigation)
        return Response(serializer)

    def retrieve_by_project(self, project_id=None):
        investigation = get_object_or_404(Investigation, project=project_id)
        serializer = InvestigationSerializer(investigation)
        return Response(serializer)

    def add_investigation(self):
        Investigation.objects.create()

    # TODO add theory to Investigation?
    def update_theory(self, theory, pk=None):
        investigation = get_object_or_404(Investigation, id=pk)

    def update_mechanism(self, mechanism, pk=None):
        # TODO add mechanism to model?
        return None

    def update_hypothesis(self, hypothesis, pk=None):
        # TODO add hypothesis to model?
        return None

    def update_model(self):
        return None

    def update_analysis(self, analysis_id, pk=None):
        # TODO add analysis to Investigation model?
        return None



