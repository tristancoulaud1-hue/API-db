from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Formation_ModuleDeFormation(base.base):
    __tablename__ = "Formation_ModuleDeFormation"
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)
    idModule = Column(Integer, ForeignKey("Module_de_Formation.idModule"), primary_key=True)