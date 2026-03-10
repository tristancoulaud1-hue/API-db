from jose import jwt, JWTError
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from database import get_db
from ldap_services import rechercher_infos, connection
import ldap_services
import models
import routers

load_dotenv()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")
CLE = os.getenv("CLE_SECRETE")

def verif_acces(login, password, db):
    conn = ldap_services.connection(login, password)
    if conn :
        user = db.query(models.Utilisateur).filter(models.Utilisateur.mail == login).first()
        if not user :
            donnees_ldap = ldap_services.rechercher_infos(login)
            if donnees_ldap:
                user = models.Utilisateur(
                    nom = donnees_ldap['nom'],
                    prenom = donnees_ldap['prenom'],
                    mail = login
                    )
                db.add(user)
                db.commit()
                db.refresh(user)
            else:
                return None
        return GenereToken(user.idUtilisateur)
    return None
    

def GenereToken(id_utilisateur):
    quinze_min = timedelta(minutes=15)
    exp = datetime.now() + quinze_min
    encode = jwt.encode({"ID": id_utilisateur, "exp": exp}, CLE, algorithm="HS256")
    return encode

async def get_current_user(token: str = Depends(oauth_scheme)):
    erreur_authentification = HTTPException(status_code=401, detail="Token invalide ou éxipré !")
    try:
        decode = jwt.decode(token, CLE, algorithms=["HS256"])
        utilisateur_id = decode.get("ID")
        if utilisateur_id is None:
            raise erreur_authentification
        return utilisateur_id
    except JWTError:
        raise erreur_authentification