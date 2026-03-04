from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import models
from pydantic import BaseModel
from auth import GenereToken, get_current_user

DATABASE_URL = "mssql+pyodbc://./ISEN?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

app = FastAPI()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class UtilisateurCreate(BaseModel):
    nom : str
    prenom : str
    mail : str
    MDP : str

class Login(BaseModel):
    mail : str
    MDP : str

class FormationCreate(BaseModel):
    titre: str
    niveaux: str

class ModuleCreate(BaseModel):
    titre: str
    durée: str

@app.get("/")
async def root():
    return {"message": "Salut, L'API fonctionne !"}

def get_db():
    db = SessionLocal()
    try:
        yield(db)
    finally:
        db.close()

@app.get("/utilisateur")
async def utilisateur(db:Session=Depends(get_db)):
    return db.query(models.Utilisateur).all()

@app.post("/utilisateur")
async def CreateUser(utilisateur:UtilisateurCreate, db: Session=Depends(get_db)):
    from passlib.context import CryptContext
    instance = CryptContext(schemes=["bcrypt"], deprecated="auto")
    MDP_hash = instance.hash(utilisateur.MDP)
    nouveau_user = models.Utilisateur(nom=utilisateur.nom, prenom=utilisateur.prenom, mail=utilisateur.mail, MDP=MDP_hash)
    db.add(nouveau_user)
    db.commit()
    db.refresh(nouveau_user)
    return nouveau_user

@app.get("/utilisateur/{id}")
async def getUtilisateur(id: int, db:Session=Depends(get_db)):
    return db.query(models.Utilisateur).filter(models.Utilisateur.idUtilisateur == id).first()

@app.put("/utilisateur/{id}")
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

@app.delete("/utilisateur/{id}")
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

@app.post("/login")
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