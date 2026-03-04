from sqlalchemy.orm import declarative_base
base = declarative_base()

from .Utilisateur import Utilisateur
from .Session_de_Formation import Session_de_Formation
from .Utilisateur_SessionDeFormation import Utilisateur_SessionDeFormation
from .Formation import Formation
from .Module_de_Formation import Module_de_Formation
from .Formation_ModuleDeFormation import Formation_ModuleDeFormation
from .Evaluation import Evaluation
from .Resultat import Resultat
from .RecommendationIA import RecommendationIA
from .Recommendation_Formation import Recommendation_Formation
from .Utilisateur_Evaluations import Utilisateur_Evaluations