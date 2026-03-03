from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Utilisateur_SessionDeFormation(base.base):
    __tablename__ = "Utilisateur_SessionDeFormation"
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"), primary_key=True)
    idSession = Column(Integer, ForeignKey("Session_de_Formation.idSession"), primary_key=True)