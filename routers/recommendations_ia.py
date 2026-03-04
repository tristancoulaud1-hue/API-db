from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from datetime import datetime
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class RecommendationIACreate(BaseModel):
    date_recommendation: datetime

@router.get("/")
async def RecommendationsIA(db: Session = Depends(get_db)):
    return db.query(models.RecommendationIA).all()

@router.post("/")
async def CreateRecommendationIA(recommendation: RecommendationIACreate, db: Session = Depends(get_db)):
    nouvelleRecommendation = models.RecommendationIA(
        date_recommendation=recommendation.date_recommendation
    )
    db.add(nouvelleRecommendation)
    db.commit()
    db.refresh(nouvelleRecommendation)
    return nouvelleRecommendation

@router.get("/{id}")
async def getRecommendationIA(id: int, db: Session = Depends(get_db)):
    recommendation = db.query(models.RecommendationIA).filter(models.RecommendationIA.idRecommendation == id).first()
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation non trouvée")
    return recommendation

@router.put("/{id}")
async def ModifRecommendationIA(id: int, recommendation_modifiee: RecommendationIACreate, db: Session = Depends(get_db)):
    recommendation_existante = db.query(models.RecommendationIA).filter(models.RecommendationIA.idRecommendation == id).first()
    if not recommendation_existante:
        raise HTTPException(status_code=404, detail="Recommendation non trouvée")
    recommendation_existante.date_recommendation = recommendation_modifiee.date_recommendation
    db.commit()
    db.refresh(recommendation_existante)
    return recommendation_existante

@router.delete("/{id}")
async def DeleteRecommendationIA(id: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    recommendation = db.query(models.RecommendationIA).filter(models.RecommendationIA.idRecommendation == id).first()
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation non trouvée")
    db.delete(recommendation)
    db.commit()
    return "Recommendation supprimée."
