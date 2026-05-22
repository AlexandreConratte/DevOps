# DOCKER ET DOCKER COMPOSE - FICHE DEVOPS

## En bref

Docker emballe une application avec ce dont elle a besoin pour tourner.

Docker Compose lance plusieurs services ensemble : API, base de donnees, cache, reverse proxy.

## Image mentale

Sans Docker :

> Chez moi ca marche, mais sur le serveur ca casse.

Avec Docker :

> On livre une boite qui contient l'application et son environnement.

L'image est la recette.

Le conteneur est le plat en train d'etre servi.

## Les mots importants

| Mot | Version simple |
|---|---|
| Image | Modele pour creer un conteneur |
| Conteneur | Application qui tourne |
| Dockerfile | Recette pour construire une image |
| Volume | Stockage persistant |
| Network | Reseau entre conteneurs |
| Registry | Stockage d'images Docker |
| Docker Compose | Fichier pour lancer plusieurs services |

## Commandes essentielles

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
docker ps
docker logs <container>
docker exec -it <container> sh
docker stop <container>
docker compose up
docker compose up -d
docker compose logs -f
docker compose down
```

## Exemple Dockerfile simple

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

## Exemple Docker Compose

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## Pourquoi les volumes sont importants

Sans volume, les donnees peuvent disparaitre quand le conteneur est supprime.

Avec un volume, PostgreSQL garde ses donnees meme si le conteneur est recree.

## Erreurs classiques

| Erreur | Pourquoi c'est un probleme |
|---|---|
| Mettre un mot de passe dans le Dockerfile | Secret visible dans l'image |
| Lancer en root sans raison | Moins securise |
| Oublier `.dockerignore` | Image trop lourde |
| Confondre image et conteneur | Debug plus difficile |
| Oublier les volumes DB | Perte de donnees |

## Niveau attendu en alternance

Tu dois savoir :

- ecrire un Dockerfile simple;
- construire une image;
- lancer un conteneur;
- exposer un port;
- lire les logs;
- entrer dans un conteneur;
- utiliser Docker Compose;
- expliquer volumes et networks.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Run image | Lance `nginx` avec Docker | Page accessible |
| Facile | Logs | Lis les logs du conteneur | Tu sais les suivre |
| Facile | Build | Cree une image simple | Image visible avec `docker images` |
| Moyen | Compose | Lance API + PostgreSQL | Les 2 services tournent |
| Moyen | Volume | Redemarre PostgreSQL sans perdre les donnees | Donnees conservees |
| Dur | Debug | Corrige une app qui ne trouve pas la DB | Cause documentee |

## Drill - 5 questions

1. Difference entre image et conteneur ?
2. A quoi sert un Dockerfile ?
3. Pourquoi utiliser Docker Compose ?
4. Pourquoi une base de donnees a besoin d'un volume ?
5. Comment lire les logs d'un conteneur ?

Validation : minimum 4/5.

## A retenir

Docker est un des meilleurs leviers pour rendre une application reproductible.

Pour une alternance, savoir dockeriser une app avec une base est deja tres vendeur.

