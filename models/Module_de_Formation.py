from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from . import base

class Module_de_Formation(base):
    __tablename__ = "Module_de_Formation"
    idModule = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    titre = Column(String(200))
    duree = Column(Time(7))