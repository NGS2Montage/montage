# File used to import all the views in the folder
# This is required for Django to keep track of all
# the models.

from .permissions import UserDetail, user_profile, ApplicationList, \
    ApplicationDetail, ApplicationCreate, ApplicationJWT, get_app_secret, get_public_key, authenticate_app

from .investigation_views import InvestigationViewSet
from .observation_views import ObservationViewSet
from .project_views import ProjectViewSet
