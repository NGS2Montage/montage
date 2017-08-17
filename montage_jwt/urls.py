from .views import get_jwt

urlpatterns = [
    url(r'^(?P<jwt_type>[a-z]+)/$', get_jwt, name='get_jwt'),
]
