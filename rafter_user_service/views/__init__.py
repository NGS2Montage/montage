# File used to import all the views in the folder
# This is required for Django to keep track of all
# the models.

from .investigation_views import InvestigationViewSet
from .observation_views import ObservationViewSet
from .project_views import ProjectViewSet
from .simple_views import ProjectStateViewSet, TeamViewSet
