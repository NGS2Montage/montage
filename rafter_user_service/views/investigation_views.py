from rafter_user_service.models import Investigation
from rest_framework import viewsets
from rafter_user_service.serializers import InvestigationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class InvestigationViewSet(APIView):

    # TODO should this method get single and groups
    def get(self, request, pk, format=None):
        investigation = Investigation.objects.all()
        serializer = InvestigationSerializer(investigation)
        return Response(serializer.data)
