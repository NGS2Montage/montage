from django.conf.urls import url
from .views import get_jwt, refresh_jwt, public_key

app_name = 'montage_jwt'
urlpatterns = [
    url(r'^(?P<jwt_type>[a-z]+)/$', get_jwt, name='get_jwt'),
    url(r'^refresh$', refresh_jwt, name='refresh_jwt'),
    url(r'^public_key$', public_key, name='public_key'),
]
