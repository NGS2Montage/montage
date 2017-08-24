from django.conf.urls import url
from .views import get_jwt

app_name = 'montage_jwt'
urlpatterns = [
    url(r'^(?P<jwt_type>[a-z]+)/$', get_jwt, name='get_jwt'),
]
