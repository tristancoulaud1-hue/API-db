from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Session_de_Formation(base):
    __tablename__ = "Session_de_Formation"
    idSession = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"))