from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Recommendation_Formation(base):
    __tablename__ = "Recommendation_Formation"
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"), primary_key=True)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)