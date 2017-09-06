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
    url(r'^', include(router.urls)),
    url(r'^profile/(?P<username>.+)/$', views.UserDetail.as_view(), name='user'),
]
