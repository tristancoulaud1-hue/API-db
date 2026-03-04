from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from datetime import datetime
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class EvaluationCreate(BaseModel):
    type: str
    date_evaluation: datetime
    idModule: int

@router.get("/")
async def Evaluations(db: Session = Depends(get_db)):
    return db.query(models.Evaluation).all()

@router.post("/")
async def CreateEvaluation(evaluation: EvaluationCreate, db: Session = Depends(get_db)):
    nouvelleEvaluation = models.Evaluation(
        type=evaluation.type,
        date_evaluation=evaluation.date_evaluation,
        idModule=evaluation.idModule
    )
    db.add(nouvelleEvaluation)
    db.commit()
    db.refresh(nouvelleEvaluation)
    return nouvelleEvaluation

@router.get("/{id}")
async def getEvaluation(id: int, db: Session = Depends(get_db)):
    evaluation = db.query(models.Evaluation).filter(models.Evaluation.idEvaluations == id).first()
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation non trouvée")
    return evaluation

@router.put("/{id}")
async def ModifEvaluation(id: int, evaluation_modifiee: EvaluationCreate, db: Session = Depends(get_db)):
    evaluation_existante = db.query(models.Evaluation).filter(models.Evaluation.idEvaluations == id).first()
    if not evaluation_existante:
        raise HTTPException(status_code=404, detail="Evaluation non trouvée")
    evaluation_existante.type = evaluation_modifiee.type
    evaluation_existante.date_evaluation = evaluation_modifiee.date_evaluation
    evaluation_existante.idModule = evaluation_modifiee.idModule
    db.commit()
    db.refresh(evaluation_existante)
    return evaluation_existante

@router.delete("/{id}")
async def DeleteEvaluation(id: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    evaluation = db.query(models.Evaluation).filter(models.Evaluation.idEvaluations == id).first()
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation non trouvée")
    db.delete(evaluation)
    db.commit()
    return "Evaluation supprimée."
