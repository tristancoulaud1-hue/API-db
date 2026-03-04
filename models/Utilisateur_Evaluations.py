from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from . import base

class Utilisateur_Evaluations(base):
    __tablename__ = "Utilisateur_Evaluations"
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"), primary_key=True)
    idEvaluations = Column(Integer,ForeignKey("Evaluations.idEvaluations"), primary_key=True)