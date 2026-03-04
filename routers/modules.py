from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class ModuleCreate(BaseModel):
    titre: str
    duree: str

@router.get("/")
async def Modules(db:Session=Depends(get_db)):
    return db.query(models.Module_de_Formation).all()

@router.post("/")
async def CreateModule(module: ModuleCreate, db:Session = Depends(get_db)):
    nouveauModule = models.Module_de_Formation(titre=module.titre, duree=module.duree)
    db.add(nouveauModule)
    db.commit()
    db.refresh(nouveauModule)
    return nouveauModule

@router.put("/{id}")
async def ModifModule(id: int, module_modifiee: ModuleCreate, db:Session = Depends(get_db)):
    module_existant = db.query(models.Module_de_Formation).filter(models.Module_de_Formation.idModule == id).first()
    if not module_existant:
        raise HTTPException(status_code=404, detail="Module non trouvée")
    else:
        module_existant.titre = module_modifiee.titre
        module_existant.duree = module_modifiee.duree
    db.commit()
    db.refresh(module_existant)
    return module_existant

@router.delete("/{id}")
async def DeleteModule(id:int, db:Session = Depends(get_db), utilisateur_id: int = Depends(get_current_user)):
    module = db.query(models.Module_de_Formation).filter(models.Module_de_Formation.idModule == id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module non trouvé.")
    else:
        db.delete(module)
        db.commit()
        return "Module supprimé."