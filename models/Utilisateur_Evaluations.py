from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Utilisateur_Evaluations(base.base):
    __tablename__ = "Utilisateur_Evaluations"
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"), primary_key=True)
    idEvaluations = Column(Integer,ForeignKey("Evaluations.idEvaluations"), primary_key=True)