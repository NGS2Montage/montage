# File used to import all the models in the folder
# This is required for Django to keep track of all
# the models.

from .analysis import Analysis
from .application import Application
from .experiment import Experiment
from .experiment_status import ExperimentStatus
from .input import Input
from .investigation_status import InvestigationStatus
from .investigator import Investigator
from .literature import Literature
from .manipulation import Manipulation
from .model import Model
from .model_status import ModelStatus
from .output import Output
from .parameter import Parameter
from .population import Population
from .profile import Profile
from .project_state import ProjectState
from .role import Role
from .team import Team
from .theory import Theory
from .treatment import Treatment
