from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from . import base

class Formation_ModuleDeFormation(base):
    __tablename__ = "Formation_ModuleDeFormation"
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True, autoincrement=False)
    idModule = Column(Integer, ForeignKey("Module_de_Formation.idModule"), primary_key=True, autoincrement=False)