from django.conf.urls import url, include
from rafter_user_service.views import ApplicationList, ApplicationCreate, \
ApplicationDetail, get_token, authenticate_app, get_public_key, UserDetail, \
user_profile

app_name = 'user'
urlpatterns = [
    url(r'^$', user_profile, name='profile'),
    url(r'^applications/$', ApplicationList.as_view(), name='apps'),
    url(r'^applications/create/$', ApplicationCreate.as_view(), name='create_app'),
    url(r'^applications/(?P<pk>[0-9]+)/$', ApplicationDetail.as_view(), name='detail_app'),
    url(r'^applications/(?P<pk>[0-9]+)/secret/$', get_token, name='secret'),
    url(r'^authenticate/(?P<pk>[0-9]+)/$', authenticate_app, name='auth_app'),
    url(r'^public_key/$', get_public_key, name='pub_key'),
    url(r'^(?P<username>.+)/$', UserDetail.as_view(), name='user'),
]
