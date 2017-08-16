from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rafter_user_service import views

router = DefaultRouter()
router.register(r'project_view', views.ProjectViewSet)
router.register(r'observation_view', views.ObservationViewSet)
router.register(r'investigation_view', views.InvestigationViewSet)

app_name = 'user'
urlpatterns = [
    url(r'^$', views.user_profile, name='profile'),
    url(r'^$', include(router.urls)),
    url(r'^applications/$', views.ApplicationList.as_view(), name='apps'),
    url(r'^applications/create/$', views.ApplicationCreate.as_view(), name='create_app'),
    url(r'^applications/(?P<pk>[0-9]+)/$', views.ApplicationDetail.as_view(), name='detail_app'),
    url(r'^applications/(?P<pk>[0-9]+)/secret/$', views.get_token, name='secret'),
    url(r'^authenticate/(?P<pk>[0-9]+)/$', views.authenticate_app, name='auth_app'),
    url(r'^public_key/$', views.get_public_key, name='pub_key'),
    url(r'^profile/(?P<username>.+)/$', views.UserDetail.as_view(), name='user'),
]
