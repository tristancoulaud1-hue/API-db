from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from datetime import datetime
from sqlalchemy import DateTime
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class SessionDeFormationCreate(BaseModel):
    date_debut: datetime
    date_fin: datetime
    idFormation: int

@router.get("/")
async def Sessions(db: Session = Depends(get_db)):
    return db.query(models.Session_de_Formation).all()

@router.post("/")
async def CreateSession(session: SessionDeFormationCreate, db: Session = Depends(get_db)):
    nouvelleSession = models.Session_de_Formation(
        date_debut=session.date_debut,
        date_fin=session.date_fin,
        idFormation=session.idFormation
    )
    db.add(nouvelleSession)
    db.commit()
    db.refresh(nouvelleSession)
    return nouvelleSession

@router.get("/{id}")
async def getSession(id: int, db: Session = Depends(get_db)):
    session = db.query(models.Session_de_Formation).filter(models.Session_de_Formation.idSession == id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    return session

@router.put("/{id}")
async def ModifSession(id: int, session_modifiee: SessionDeFormationCreate, db: Session = Depends(get_db)):
    session_existante = db.query(models.Session_de_Formation).filter(models.Session_de_Formation.idSession == id).first()
    if not session_existante:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    session_existante.date_debut = session_modifiee.date_debut
    session_existante.date_fin = session_modifiee.date_fin
    session_existante.idFormation = session_modifiee.idFormation
    db.commit()
    db.refresh(session_existante)
    return session_existante

@router.delete("/{id}")
async def DeleteSession(id: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    session = db.query(models.Session_de_Formation).filter(models.Session_de_Formation.idSession == id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    db.delete(session)
    db.commit()
    return "Session supprimée."
