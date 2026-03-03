from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Formation(base):
    __tablename__ = "Formation"
    idFormation = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    titre = Column(String(200))
    niveaux = Column(String(50))