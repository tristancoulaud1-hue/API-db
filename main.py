from fastapi import FastAPI
import models
from pydantic import BaseModel
from routers import (
    utilisateurs, formations, login, modules,
    sessions_de_formation, evaluations, resultats,
    recommendations_ia, utilisateurs_sessions,
    formations_modules, recommendations_formations,
    utilisateurs_evaluations
)

app = FastAPI()

app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(formations.router, prefix="/formations", tags=["Formations"])
app.include_router(modules.router, prefix="/modules", tags=["Modules"])
app.include_router(login.router, prefix="/login", tags=["Login"])
app.include_router(sessions_de_formation.router, prefix="/sessions", tags=["Sessions de Formation"])
app.include_router(evaluations.router, prefix="/evaluations", tags=["Evaluations"])
app.include_router(resultats.router, prefix="/resultats", tags=["Resultats"])
app.include_router(recommendations_ia.router, prefix="/recommendations-ia", tags=["Recommendations IA"])
app.include_router(utilisateurs_sessions.router, prefix="/utilisateurs-sessions", tags=["Utilisateurs Sessions"])
app.include_router(formations_modules.router, prefix="/formations-modules", tags=["Formations Modules"])
app.include_router(recommendations_formations.router, prefix="/recommendations-formations", tags=["Recommendations Formations"])
app.include_router(utilisateurs_evaluations.router, prefix="/utilisateurs-evaluations", tags=["Utilisateurs Evaluations"])

@app.get("/")
async def root():
    return {"message": "Salut, L'API fonctionne !"}