from rafter_user_service.models import Observation
from rest_framework import viewsets
from rafter_user_service.serializers import ObservationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


class ObservationViewSet(viewsets.ModelViewSet):

    serializer_class = ObservationSerializer
    queryset = Observation.objects.all()

    def retrieve_observation(self, pk=None):
        observation = get_object_or_404(Observation, pk=pk)
        serializer = ObservationSerializer(observation)
        return Response(serializer)

    def retrieve_observations(self, project_id=None):
        investigation = get_object_or_404(Observation, project=project_id)
        serializer = ObservationSerializer(investigation)
        return Response(serializer)
