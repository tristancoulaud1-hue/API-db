from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from . import base

class Recommendation_Formation(base):
    __tablename__ = "Recommendation_Formation"
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"), primary_key=True)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)