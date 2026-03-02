from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Time
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Utilisateur(base):
    __tablename__ = "Utilisateur"
    idUtilisateur = Column(Integer, primary_key=True)
    nom = Column(String(300))
    prénom = Column(String(300))
    mail = Column(String(264))
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"))

class RecommendationIA(base):
    __tablename__ = "RecommendationIA"
    idRecommendation = Column(Integer, primary_key=True)
    date_recommendation = Column(DateTime)

class Formation(base):
    __tablename__ = "Formation"
    idFormation = Column(Integer, primary_key=True)
    titre = Column(String(200))
    niveaux = Column(String(50))

class Session_de_Formation(base):
    __tablename__ = "Session_de_Formation"
    idSession = Column(Integer, primary_key=True)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"))

class Utilisateur_SessionDeFormation(base):
    __tablename__ = "Utilisateur_SessionDeFormation"
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"), primary_key=True)
    idSession = Column(Integer, ForeignKey("Session_de_Formation.idSession"), primary_key=True)

class Formation_ModuleDeFormation(base):
    __tablename__ = "Formation_ModuleDeFormation"
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)
    idModule = Column(Integer, ForeignKey("Module_de_Formation.idModule"), primary_key=True)

class Module_de_Formation(base):
    __tablename__ = "Module_de_Formation"
    idModule = Column(Integer, primary_key=True)
    titre = Column(String(200))
    duree = Column(Time(7))

class Evaluation(base):
    __tablename__ = "Evaluations"
    idEvaluations = Column(Integer, primary_key=True)
    type = Column(String(50))
    date_evaluation = Column(DateTime)
    idModule = Column(Integer, ForeignKey("Module_de_Formation.idModule"))

class Resultat(base):
    __tablename__ = "Resultat"
    idResultat = Column(Integer, primary_key=True)
    score = Column(Integer)
    reussite = Column(String(50))
    date_resultat = Column(DateTime)
    idEvaluations = Column(Integer, ForeignKey("Evaluations.idEvaluations"))
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"))

class Recommendation_Formation(base):
    __tablename__ = "Recommendation_Formation"
    idRecommendation = Column(Integer, ForeignKey("RecommendationIA.idRecommendation"), primary_key=True)
    idFormation = Column(Integer, ForeignKey("Formation.idFormation"), primary_key=True)

class Utilisateur_Evaluations(base):
    __tablename__ = "Utilisateur_Evaluations"
    idUtilisateur = Column(Integer, ForeignKey("Utilisateur.idUtilisateur"), primary_key=True)
    idEvaluations = Column(Integer,ForeignKey("Evaluations.idEvaluations"), primary_key=True)