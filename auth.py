import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def GenereToken(id_utilisateur):
    CLE = os.getenv("CLE_SECRETE")
    quinze_min = timedelta(minutes=15)
    exp = datetime.now() + quinze_min
    encode = jwt.encode({"ID": id_utilisateur, "exp": exp}, CLE, algorithm="HS256")
    return encode