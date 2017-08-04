from rafter_user_service.models import Project
from rest_framework import viewsets
from rafter_user_service.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectViewSet(APIView):

    # TODO should this method get single and groups?
    def get(self, request, pk, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)

    # TODO Create and Update
    def put(self, request, pk, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)
