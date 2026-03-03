from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Session_de_Formation(base.base):
    __tablename__ = "Session_de_Formation"
    idSession = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"))