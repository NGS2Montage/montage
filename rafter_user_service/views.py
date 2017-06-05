from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rafter_user_service.models import Application, Profile
from rafter_user_service.serializers import ApplicationJWTSerializer, ApplicationSerializer
from rafter_user_service.permissions import IsOwnerOrPost

# Create your views here.
class ApplicationList(ListView):
    model = Application

class ApplicationDetail(DetailView):
    model = Application

class ApplicationCreate(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ApplicationJWT(APIView):
    serializer_class = ApplicationJWTSerializer
    permission_classes = (IsOwnerOrPost,)

    def get(self, request, pk, *args, **kwargs):
        app = get_object_or_404(Application, pk=pk)
        self.check_object_permissions(request, app)
        data = {
            'token': app.get_user_token()
        }
        return Response(data)

    def post(self, request, pk, *args, **kwargs):
        app = get_object_or_404(Application, pk=pk)
        self.check_object_permissions(request, app)
        context = {
            'app': app
        }
        serializer = self.serializer_class(data=request.data, context=context)

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors)
            

authenticate_app = ApplicationJWT.as_view()

@api_view(['GET'])
def get_token(request, pk):
    app = get_object_or_404(Application, pk=pk)

    if not app.user == request.user:
        raise PermissionDenied()

    token = app.generate_access_token()
    app.save()
    data = {
        'app_id': pk,
        'app_secret': token,
    }
    return Response(data)

@api_view(['GET'])
def get_public_key(request):
    if api_settings.JWT_PUBLIC_KEY:
        pub_key = api_settings.JWT_PUBLIC_KEY
        data = {
            'key': pub_key
        }
        return Response(data)
    
    raise Http404('No public key.')
