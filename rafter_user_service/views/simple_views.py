from rest_framework import viewsets

from rafter_user_service import models, serializers


class ProjectStateViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProjectStateSerializer
    queryset = models.ProjectState.objects.all()


class TeamViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()
