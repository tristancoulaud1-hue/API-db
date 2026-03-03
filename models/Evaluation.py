from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base
from models.Module_de_Formation import Module_de_Formation

class Evaluation(base.base):
    __tablename__ = "Evaluations"
    idEvaluations = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    type = Column(String(50))
    date_evaluation = Column(DateTime)
    idModule = Column(Integer, ForeignKey("Module_de_Formation.idModule"))