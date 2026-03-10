from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import get_current_user

router = APIRouter()

class UtilisateurCreate(BaseModel):
    nom : str
    prenom : str
    mail : str

@router.get("/")
async def utilisateur(db:Session=Depends(get_db)):
    return db.query(models.Utilisateur).all()

@router.post("/")
async def CreateUser(utilisateur:UtilisateurCreate, db: Session=Depends(get_db)):
    nouveau_user = models.Utilisateur(nom=utilisateur.nom, prenom=utilisateur.prenom, mail=utilisateur.mail)
    db.add(nouveau_user)
    db.commit()
    db.refresh(nouveau_user)
    return nouveau_user

@router.get("/{id}")
async def getUtilisateur(id: int, db:Session=Depends(get_db)):
    return db.query(models.Utilisateur).filter(models.Utilisateur.idUtilisateur == id).first()

@router.put("/{id}")
async def ModifUtilisateur(donnesModifiees: UtilisateurCreate, id: int, db:Session=Depends(get_db)):
    utilisateur = await getUtilisateur(id, db)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    else:
        utilisateur.nom = donnesModifiees.nom
        utilisateur.prenom = donnesModifiees.prenom
        utilisateur.mail = donnesModifiees.mail
        db.commit()
        db.refresh(utilisateur)
    return utilisateur

@router.delete("/{id}")
async def SuppUtilisateur(
    id: int, db:Session=Depends(get_db),
    utilisateur_id: int = Depends(get_current_user)
    ):
    utilisateur = await getUtilisateur(id, db)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    else:
        db.delete(utilisateur)
        db.commit()
    return "Utilisateurs Supprimé"

@router.get("/mon_compte")
async def voir_profil(user_id: int = Depends(get_current_user)):
    return {"message": f"Bonjour utilisateur numéro {user_id}"}