from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, NotFound
from rest_framework.permissions import AllowAny
from montage_jwt.util import make_claims, refresh
from montage_jwt.models import JWT
from montage_jwt.serializers import JWTSerializer
from montage_jwt.settings import api_settings

# Create your views here.

@api_view(['GET'])
def public_key(request):
    key = api_settings.PUBLIC_KEY
    return Response(key)


@api_view(['GET'])
def get_jwt(request, jwt_type):
    user = request.user

    if not user.is_authenticated:
        raise NotAuthenticated(detail='User not logged in.')
    
    jwt_type = jwt_type.upper()  

    try:
        claims = make_claims(user, jwt_type)
    except ValueError:
        raise NotFound(detail='{} is not a valid JWT type.'.format(jwt_type))

    jwt = JWT.objects.create_token(claims, user)

    return Response({
        'token': jwt.token
    })


@permission_classes([AllowAny,])
@api_view(['POST'])
def refresh_jwt(request):
    serializer = JWTSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    valid = serializer.data
    claims = serializer.claims

    jwt = refresh(claims)

    return Response({
        'token': jwt.token,
    })
