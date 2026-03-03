from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Resultat(base.base):
    __tablename__ = "Resultat"
    idResultat = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    score = Column(Integer)
    reussite = Column(String(50))
    date_resultat = Column(DateTime)
    idEvaluations = Column(Integer, ForeignKey("Evaluations.idEvaluations"))
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"))