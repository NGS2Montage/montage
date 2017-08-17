from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import make_token

# Create your views here.

@api_view(['GET'])
def get_jwt(request, jwt_type):
    user = request.user

    if not user.is_authenticated:
        return Response({
            'error': 'User not logged in.'
        })

    token = make_token(user, jwt_type)

    return Response({
        'token': token
    })
