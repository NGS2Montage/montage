from rafter_user_service.models import Investigation
from rest_framework import viewsets
from rafter_user_service.serializers import InvestigationSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class InvestigationViewSet(viewsets.ViewSet):

    def retrieve_investigation(self, pk=None):
        investigation = get_object_or_404(Investigation, pk=pk)
        serializer = InvestigationSerializer(investigation)
        return Response(serializer)

    def retrieve_by_project(self, project_id=None):
        investigation = get_object_or_404(Investigation, project=project_id)
        serializer = InvestigationSerializer(investigation)
        return Response(serializer)
