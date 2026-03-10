from ldap3 import Server, Connection
from dotenv import load_dotenv
import os

load_dotenv()
server = Server("192.168.170.10")
domaine = "isen.fr"


def connection(login, password):
    DN = f"{login}@{domaine}"
    try:
        with Connection(server=server, user=DN, password=password) as connexion :
            resultat = connexion.bind()
    except:
        resultat = False
    return resultat

def rechercher_infos(login):
    DN = f"{login}@{domaine}"
    with Connection(server=server, user = DN, password="S1pln83!") as connexion :
        connexion.bind()
        connexion.search(search_base='dc=isen,dc=fr', 
                                    search_filter=f"(sAMAccountName={login})", 
                                    attributes=['sn', 'givenName', 'mail']
                                    )
        if connexion.entries:
            entree = connexion.entries[0]
            donnees = {
                "prenom": str(entree.givenName),
                "nom":str(entree.sn),
                "mail": str(entree.mail)
            }
            return donnees
        else:
            return None

print(connection(os.getenv("LOGIN"), os.getenv("PASSWORD")))