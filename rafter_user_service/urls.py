from django.conf.urls import url
from rafter_user_service.views import ApplicationList, ApplicationCreate, \
ApplicationDetail, get_token, authenticate_app, get_public_key

app_name = 'user'
urlpatterns = [
    url(r'^applications/$', ApplicationList.as_view(), name='apps'),
    url(r'^applications/create/$', ApplicationCreate.as_view(), name='create_app'),
    url(r'^applications/(?P<pk>[0-9]+)/$', ApplicationDetail.as_view(), name='detail_app'),
    url(r'^applications/(?P<pk>[0-9]+)/secret/$', get_token, name='secret'),
    url(r'^authenticate/(?P<pk>[0-9]+)/$', authenticate_app, name='auth_app'),
    url(r'^public_key/$', get_public_key, name='pub_key')
]
