from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models
from database import get_db
from auth import verif_acces

router = APIRouter()

class Login(BaseModel):
    mail : str
    MDP : str

@router.post("/")
async def login_route(login: Login, db: Session = Depends(get_db)):
    token = verif_acces(login.mail, login.MDP, db)
    if not token:
        raise HTTPException(status_code=401, detail="Identifiants incorrects ou accès refusé")
    return {"access_token": token, "token_type": "bearer"}