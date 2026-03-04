from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from datetime import datetime
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class ResultatCreate(BaseModel):
    score: int
    reussite: str
    date_resultat: datetime
    idEvaluations: int
    idUtilisateur: int

@router.get("/")
async def Resultats(db: Session = Depends(get_db)):
    return db.query(models.Resultat).all()

@router.post("/")
async def CreateResultat(resultat: ResultatCreate, db: Session = Depends(get_db)):
    nouveauResultat = models.Resultat(
        score=resultat.score,
        reussite=resultat.reussite,
        date_resultat=resultat.date_resultat,
        idEvaluations=resultat.idEvaluations,
        idUtilisateur=resultat.idUtilisateur
    )
    db.add(nouveauResultat)
    db.commit()
    db.refresh(nouveauResultat)
    return nouveauResultat

@router.get("/{id}")
async def getResultat(id: int, db: Session = Depends(get_db)):
    resultat = db.query(models.Resultat).filter(models.Resultat.idResultat == id).first()
    if not resultat:
        raise HTTPException(status_code=404, detail="Resultat non trouvé")
    return resultat

@router.put("/{id}")
async def ModifResultat(id: int, resultat_modifie: ResultatCreate, db: Session = Depends(get_db)):
    resultat_existant = db.query(models.Resultat).filter(models.Resultat.idResultat == id).first()
    if not resultat_existant:
        raise HTTPException(status_code=404, detail="Resultat non trouvé")
    resultat_existant.score = resultat_modifie.score
    resultat_existant.reussite = resultat_modifie.reussite
    resultat_existant.date_resultat = resultat_modifie.date_resultat
    resultat_existant.idEvaluations = resultat_modifie.idEvaluations
    resultat_existant.idUtilisateur = resultat_modifie.idUtilisateur
    db.commit()
    db.refresh(resultat_existant)
    return resultat_existant

@router.delete("/{id}")
async def DeleteResultat(id: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    resultat = db.query(models.Resultat).filter(models.Resultat.idResultat == id).first()
    if not resultat:
        raise HTTPException(status_code=404, detail="Resultat non trouvé")
    db.delete(resultat)
    db.commit()
    return "Resultat supprimé."
