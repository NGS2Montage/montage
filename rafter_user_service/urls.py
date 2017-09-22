from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rafter_user_service import views

router = DefaultRouter()
router.register(r'analyses', views.AnalysisViewSet)
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'hypotheses', views.HypothesisViewSet)
router.register(r'investigations', views.InvestigationViewSet)
router.register(r'mechanisms', views.MechanismViewSet)
router.register(r'observations', views.ObservationViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'theories', views.TheoryViewSet)

app_name = 'user'
urlpatterns = [
    url(r'^', include(router.urls)),
]
