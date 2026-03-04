from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class UtilisateurSessionCreate(BaseModel):
    idUtilisateur: int
    idSession: int

@router.get("/")
async def UtilisateursSessions(db: Session = Depends(get_db)):
    return db.query(models.Utilisateur_SessionDeFormation).all()

@router.post("/")
async def CreateUtilisateurSession(utilisateur_session: UtilisateurSessionCreate, db: Session = Depends(get_db)):
    # Vérifier que l'utilisateur et la session existent
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.idUtilisateur == utilisateur_session.idUtilisateur).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    session = db.query(models.Session_de_Formation).filter(models.Session_de_Formation.idSession == utilisateur_session.idSession).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    
    nouvelleAssociation = models.Utilisateur_SessionDeFormation(
        idUtilisateur=utilisateur_session.idUtilisateur,
        idSession=utilisateur_session.idSession
    )
    db.add(nouvelleAssociation)
    db.commit()
    db.refresh(nouvelleAssociation)
    return nouvelleAssociation

@router.get("/{idUtilisateur}/{idSession}")
async def getUtilisateurSession(idUtilisateur: int, idSession: int, db: Session = Depends(get_db)):
    association = db.query(models.Utilisateur_SessionDeFormation).filter(
        models.Utilisateur_SessionDeFormation.idUtilisateur == idUtilisateur,
        models.Utilisateur_SessionDeFormation.idSession == idSession
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return association

@router.delete("/{idUtilisateur}/{idSession}")
async def DeleteUtilisateurSession(idUtilisateur: int, idSession: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    association = db.query(models.Utilisateur_SessionDeFormation).filter(
        models.Utilisateur_SessionDeFormation.idUtilisateur == idUtilisateur,
        models.Utilisateur_SessionDeFormation.idSession == idSession
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    db.delete(association)
    db.commit()
    return "Association supprimée."
