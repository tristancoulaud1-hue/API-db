from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time, Identity
from sqlalchemy.orm import declarative_base

base = declarative_base()

class RecommendationIA(base):
    __tablename__ = "RecommendationIA"
    idRecommendation = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    date_recommendation = Column(DateTime)