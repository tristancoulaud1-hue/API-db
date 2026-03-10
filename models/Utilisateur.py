from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from sqlalchemy.orm import relationship
from . import base

class Utilisateur(base):
    __tablename__ = "Utilisateur"
    idUtilisateur = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    nom = Column(String(300))
    prenom = Column(String(300))
    mail = Column(String(264))
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"))
    sessions = relationship(
        "Session_de_Formation",
        secondary = "Utilisateur_SessionDeFormation",
        back_populates = "participants"
    )