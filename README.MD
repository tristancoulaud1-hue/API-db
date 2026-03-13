# API de Gestion de Données - Version Python (FastAPI/Flask)

Ce dépôt contient la version **Python** de l'architecture Dual-Stack. Cette implémentation a été conçue pour offrir une alternative agile et flexible à la version .NET Core, facilitant l'intégration future de modules d'Analyse de Données et d'Intelligence Artificielle.

## Technologies Utilisées
* **Framework** : FastAPI (ou Flask)
* **ORM** : SQLAlchemy (Accès aux données)
* **Sécurité** : PyJWT pour la gestion des tokens
* **Validation** : Pydantic (pour le typage des données)

## Architecture & Philosophie
Contrairement au piler industriel .NET, la version Python privilégie :
* **L'interopérabilité** : Utilise la même base de données SQL Server que la version .NET.
* **L'extensibilité** : Structure prête pour l'intégration de bibliothèques comme Pandas ou Scikit-Learn.
* **La Légèreté** : Moins de boilerplate pour une exécution rapide des scripts de maintenance.

## Installation & Démarrage

### Prérequis
* Python 3.10+
* Un environnement virtuel (`venv`) recommandé

### Configuration

1. Créez et activez l'environnement virtuel :

```Bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

2. Installez les dépendances :

```Bash
pip install -r requirements.txt
```

3. Lancez le serveur :

```Bash
python app.py  # ou uvicorn main:app --reload
```

## Sécurité & Conformité
- **Validation Rigoureuse** : Les schémas Pydantic assurent que les données entrantes correspondent aux modèles SQL.

- **Gestion des Erreurs** : Middlewares personnalisés pour éviter l'exposition des stacktraces en production.

- **SQLAlchemy** : Protection native contre les injections SQL par l'utilisation de requêtes paramétrées.