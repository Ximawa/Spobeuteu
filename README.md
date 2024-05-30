# Traitement et analyse de données du Spotify Millions Playlist Dataset

## Peuplage de la base de données (BDD)

Se déplacer dans le dossier correspondant 
```
cd Spobeuteu_peuplage_BDD
```

Les informations de la BDD se situent dans le fichier .env, à modifier là-bas si nécessaire (elles ont le setup par défaut).

### Installation des dépendances
```
pip install -r requirements.txt
```

### Création de la BDD et des tables
```
py models.py
```

### Peuplage de la BDD
Il vous faudra ajouter le dossier data contenant les json du dataset dans le dossier comme ceci : Spobeuteu/Spobeuteu_peuplage_BDD/data/
Par défaut, le script va remplir la BDD avec 5 fichiers JSON, mais cela est paramétrable dans le fichier .env
```
py main.py
```

## API et visualisation des données
J'ai pu déployer une version de l'API et du front à l'adresse suivante : http://213.210.20.120/ (Pas de nom de domaine non plus heho)

Cette version est peuplée avec 5000 playlists afin de réduire le temps d'exécution des requêtes.

Vous pouvez tester les requêtes directement à l'aide de Swagger à l'adresse suivante : http://213.210.20.120:8000/docs

Sinon, vous pouvez le lancer en local avec la BDD que vous avez créée et peuplée ci-dessus.

## Backend

```
cd ../Spobeuteu_BACK
```
### Installation des dépendances
```
pip install -r requirements.txt
```
### Lancement de l'API
```
uvicorn app.main:app
```

Une fois l'API lancée, Swagger sera accessible à l'adresse suivante : http://localhost:8000/docs

## Frontend

Dans un autre terminal
```
cd Spobeuteu_FRONT
```
### Installation des dépendances
```
npm install
```
### Lancement du serveur front
```
npm start
```
