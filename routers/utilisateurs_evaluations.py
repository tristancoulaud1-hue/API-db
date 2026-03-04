from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class UtilisateurEvaluationCreate(BaseModel):
    idUtilisateur: int
    idEvaluations: int

@router.get("/")
async def UtilisateurEvaluations(db: Session = Depends(get_db)):
    return db.query(models.Utilisateur_Evaluations).all()

@router.post("/")
async def CreateUtilisateurEvaluation(utilisateur_evaluation: UtilisateurEvaluationCreate, db: Session = Depends(get_db)):
    # Vérifier que l'utilisateur et l'évaluation existent
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.idUtilisateur == utilisateur_evaluation.idUtilisateur).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    evaluation = db.query(models.Evaluation).filter(models.Evaluation.idEvaluations == utilisateur_evaluation.idEvaluations).first()
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation non trouvée")
    
    nouvelleAssociation = models.Utilisateur_Evaluations(
        idUtilisateur=utilisateur_evaluation.idUtilisateur,
        idEvaluations=utilisateur_evaluation.idEvaluations
    )
    db.add(nouvelleAssociation)
    db.commit()
    db.refresh(nouvelleAssociation)
    return nouvelleAssociation

@router.get("/{idUtilisateur}/{idEvaluations}")
async def getUtilisateurEvaluation(idUtilisateur: int, idEvaluations: int, db: Session = Depends(get_db)):
    association = db.query(models.Utilisateur_Evaluations).filter(
        models.Utilisateur_Evaluations.idUtilisateur == idUtilisateur,
        models.Utilisateur_Evaluations.idEvaluations == idEvaluations
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return association

@router.delete("/{idUtilisateur}/{idEvaluations}")
async def DeleteUtilisateurEvaluation(idUtilisateur: int, idEvaluations: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    association = db.query(models.Utilisateur_Evaluations).filter(
        models.Utilisateur_Evaluations.idUtilisateur == idUtilisateur,
        models.Utilisateur_Evaluations.idEvaluations == idEvaluations
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    db.delete(association)
    db.commit()
    return "Association supprimée."
