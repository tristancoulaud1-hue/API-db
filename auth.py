import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def GenereToken():
    CLE = os.getenv("CLE_SECRETE")
    quinze_min = timedelta(minutes=15)
    exp = datetime.now() + quinze_min
    encode = jwt.encode({"ID": 1, "exp": exp}, CLE, algorithm="HS256")
    jwt.decode(encode, CLE, algorithms="HS256")

GenereToken()