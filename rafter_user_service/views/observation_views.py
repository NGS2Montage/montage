from rafter_user_service.models import Observation
from rafter_user_service.serializers import ObservationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ObservationViewSet(APIView):
    
    # TODO should this method get single and groups
    def get(self, request, pk, format=None):
        investigation = Observation.objects.all()
        serializer = ObservationSerializer(investigation)
        return Response(serializer.data)
