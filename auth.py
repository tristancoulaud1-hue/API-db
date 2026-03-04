from jose import jwt, JWTError
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

load_dotenv()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")
CLE = os.getenv("CLE_SECRETE")

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