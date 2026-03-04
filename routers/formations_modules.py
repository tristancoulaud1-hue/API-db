from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class FormationModuleCreate(BaseModel):
    idFormation: int
    idModule: int

@router.get("/")
async def FormationsModules(db: Session = Depends(get_db)):
    return db.query(models.Formation_ModuleDeFormation).all()

@router.post("/")
async def CreateFormationModule(formation_module: FormationModuleCreate, db: Session = Depends(get_db)):
    # Vérifier que la formation et le module existent
    formation = db.query(models.Formation).filter(models.Formation.idFormation == formation_module.idFormation).first()
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    
    module = db.query(models.Module_de_Formation).filter(models.Module_de_Formation.idModule == formation_module.idModule).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module non trouvé")
    
    nouvelleAssociation = models.Formation_ModuleDeFormation(
        idFormation=formation_module.idFormation,
        idModule=formation_module.idModule
    )
    db.add(nouvelleAssociation)
    db.commit()
    db.refresh(nouvelleAssociation)
    return nouvelleAssociation

@router.get("/{idFormation}/{idModule}")
async def getFormationModule(idFormation: int, idModule: int, db: Session = Depends(get_db)):
    association = db.query(models.Formation_ModuleDeFormation).filter(
        models.Formation_ModuleDeFormation.idFormation == idFormation,
        models.Formation_ModuleDeFormation.idModule == idModule
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return association

@router.delete("/{idFormation}/{idModule}")
async def DeleteFormationModule(idFormation: int, idModule: int, db: Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    association = db.query(models.Formation_ModuleDeFormation).filter(
        models.Formation_ModuleDeFormation.idFormation == idFormation,
        models.Formation_ModuleDeFormation.idModule == idModule
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    db.delete(association)
    db.commit()
    return "Association supprimée."
