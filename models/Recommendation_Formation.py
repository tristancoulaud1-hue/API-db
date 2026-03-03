from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from models import base

class Recommendation_Formation(base.base):
    __tablename__ = "Recommendation_Formation"
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"), primary_key=True)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)