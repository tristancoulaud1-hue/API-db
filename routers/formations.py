from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class FormationCreate(BaseModel):
    titre: str
    niveaux: str

@router.get("/")
async def Formation(db:Session=Depends(get_db)):
    return db.query(models.Formation).all()

@router.post("/")
async def CreateFormation(formation: FormationCreate, db:Session = Depends(get_db)):
    nouvelleFormation = models.Formation(titre=formation.titre, niveaux=formation.niveaux)
    db.add(nouvelleFormation)
    db.commit()
    db.refresh(nouvelleFormation)
    return nouvelleFormation

@router.put("/{id}")
async def ModifFormation(id: int, formation_modifiee: FormationCreate, db:Session = Depends(get_db)):
    formation_existante = db.query(models.Formation).filter(models.Formation.idFormation == id).first()
    if not formation_existante:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    else:
        formation_existante.titre = formation_modifiee.titre
        formation_existante.niveaux = formation_modifiee.niveaux
    db.commit()
    db.refresh(formation_existante)
    return formation_existante

@router.delete("/{id}")
async def DeleteFormation(id:int, db:Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    formation = db.query(models.Formation).filter(models.Formation.idFormation == id).first()
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    else:
        db.delete(formation)
        db.commit()
        return "Formation supprimée."