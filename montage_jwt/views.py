from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from montage_jwt.util import make_claims
from montage_jwt.models import JWT

# Create your views here.

@api_view(['GET'])
def get_jwt(request, jwt_type):
    user = request.user

    if not user.is_authenticated:
        return Response({
            'error': 'User not logged in.'
        })
    
    jwt_type = jwt_type.upper()  

    try:
        claims = make_claims(user, jwt_type)
    except ValueError:
        return Response({
            'error': '{} is not a valid JWT type.'.format(jwt_type),
        })

    jwt = JWT.objects.create_token(claims, user)

    return Response({
        'token': jwt.token
    })
