from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import base, Utilisateur
from pydantic import BaseModel

DATABASE_URL = "mssql+pyodbc://./ISEN?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

app = FastAPI()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class UtilisateurCreate(BaseModel):
    nom : str
    prénom : str
    mail : str

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
    return db.query(Utilisateur).all()

@app.post("/utilisateur")
async def CreateUser(utilisateur:UtilisateurCreate, db: Session=Depends(get_db)):
    nouveau_user = Utilisateur(nom=utilisateur.nom, prénom=utilisateur.prénom, mail=utilisateur.mail)
    db.add(nouveau_user)
    db.commit()
    db.refresh(nouveau_user)
    return nouveau_user

@app.get("/utilisateur/{id}")
async def getUtilisateur(id: int, db:Session=Depends(get_db)):
    return db.query(Utilisateur).filter(Utilisateur.idUtilisateur == id).first()

@app.put("/utilisateur/{id}")
async def ModifUtilisateur(donnesModifiees: UtilisateurCreate, id: int, db:Session=Depends(get_db)):
    utilisateur = await getUtilisateur(id, db)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    else:
        utilisateur.nom = donnesModifiees.nom
        utilisateur.prénom = donnesModifiees.prénom
        utilisateur.mail = donnesModifiees.mail
        db.commit()
        db.refresh(utilisateur)
    return utilisateur

@app.delete("/utilisateur/{id}")
async def SuppUtilisateur(id: int, db:Session=Depends(get_db)):
    utilisateur = await getUtilisateur(id, db)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    else:
        db.delete(utilisateur)
        db.commit()
    return "Utilisateurs Supprimé"