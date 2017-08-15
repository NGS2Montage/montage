from rafter_user_service.models import Project
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rafter_user_service.serializers import ProjectSerializer
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

class ProjectViewSet(viewsets.ViewSet):

    serializer_class = ProjectSerializer

    def retrieve_project(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer)

    def retrieve_projects(self, request, pk=None):
        serializer = ProjectSerializer(Project.objects.all())
        return Response(serializer)
