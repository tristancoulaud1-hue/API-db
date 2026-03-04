from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import GenereToken

router = APIRouter()

class Login(BaseModel):
    mail : str
    MDP : str

@router.post("/")
async def token(login: Login, db: Session=Depends(get_db)):
    from passlib.context import CryptContext
    instance = CryptContext(schemes=["bcrypt"], deprecated="auto")
    email = login.mail
    MDP = login.MDP
    utilisateur_trouve = db.query(models.Utilisateur).filter(models.Utilisateur.mail == email).first()
    if utilisateur_trouve == None:
        raise HTTPException(status_code=401, detail="Connexions non-autorisé")
    else:
        if not instance.verify(MDP, utilisateur_trouve.MDP):
            raise HTTPException(status_code=401, detail="Connexions non-autorisé")
        else:
            token = GenereToken(utilisateur_trouve.idUtilisateur)
            return {"acces_token": token, "token_type": "bearer"}