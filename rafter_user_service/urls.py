from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rafter_user_service import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'observations', views.ObservationViewSet)
router.register(r'investigations', views.InvestigationViewSet)
router.register(r'project_states', views.ProjectStateViewSet)
router.register(r'teams', views.TeamViewSet)

app_name = 'user'
urlpatterns = [
    url(r'^', include(router.urls)),
]
