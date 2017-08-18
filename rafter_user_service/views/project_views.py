from rafter_user_service.models import Project
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rafter_user_service.serializers import ProjectSerializer
from ..models import Observation
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView


# class ProjectViewSet(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
#
#     serializer_class = ProjectSerializer
#
#     # TODO should this method get single and groups?
#     def get(self, request, pk, format=None):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects)
#         return Response(serializer.data)
#
#     # TODO Create and Update
#     def put(self, request, pk, format=None):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects)
#         return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def retrieve_project(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer)

    def retrieve_projects(self, request, pk=None):
        serializer = ProjectSerializer(Project.objects.all())
        return Response(serializer)

    def create_project(self):
        project = Project.objects.create()

    def update_project(self, pk=None):
        project = get_object_or_404(Project, pk=pk)
        project.save()

    def add_observation(self, observation_id=None, pk=None):
        observation = get_object_or_404(Observation, id=observation_id)
        project = get_object_or_404(Project, id=pk)
        # TODO need to add observation to Project
