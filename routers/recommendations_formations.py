from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class RecommendationFormationCreate(BaseModel):
    idRecommendation: int
    idFormation: int

@router.get("/")
async def RecommendationsFormations(db: Session = Depends(get_db)):
    return db.query(models.Recommendation_Formation).all()

@router.post("/")
async def CreateRecommendationFormation(recommendation_formation: RecommendationFormationCreate, db: Session = Depends(get_db)):
    # Vérifier que la recommendation et la formation existent
    recommendation = db.query(models.RecommendationIA).filter(models.RecommendationIA.idRecommendation == recommendation_formation.idRecommendation).first()
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation non trouvée")
    
    formation = db.query(models.Formation).filter(models.Formation.idFormation == recommendation_formation.idFormation).first()
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    
    nouvelleAssociation = models.Recommendation_Formation(
        idRecommendation=recommendation_formation.idRecommendation,
        idFormation=recommendation_formation.idFormation
    )
    db.add(nouvelleAssociation)
    db.commit()
    db.refresh(nouvelleAssociation)
    return nouvelleAssociation

@router.get("/{idRecommendation}/{idFormation}")
async def getRecommendationFormation(idRecommendation: int, idFormation: int, db: Session = Depends(get_db)):
    association = db.query(models.Recommendation_Formation).filter(
        models.Recommendation_Formation.idRecommendation == idRecommendation,
        models.Recommendation_Formation.idFormation == idFormation
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return association

@router.delete("/{idRecommendation}/{idFormation}")
async def DeleteRecommendationFormation(idRecommendation: int, idFormation: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    association = db.query(models.Recommendation_Formation).filter(
        models.Recommendation_Formation.idRecommendation == idRecommendation,
        models.Recommendation_Formation.idFormation == idFormation
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    db.delete(association)
    db.commit()
    return "Association supprimée."
