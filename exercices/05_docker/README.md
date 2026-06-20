# EXERCICES 05 - DOCKER AVEC DYMA

Ce dossier adapte la formation Dyma Docker au parcours DevOps.

Objectif : transformer chaque chapitre en preuve concrete dans Git, pas seulement regarder les videos.

Prerequis conseilles avant de commencer :

- etre a l'aise avec le terminal Linux;
- savoir faire des commits Git propres;
- comprendre les bases HTTP : port, localhost, requete;
- avoir vu les bases YAML et PostgreSQL avant Docker Compose avance.

## Methode

Pour chaque chapitre Dyma :

1. regarder la partie du cours;
2. refaire les manipulations dans la VM Linux;
3. noter les commandes dans ce dossier;
4. garder les erreurs interessantes;
5. committer quand le resultat fonctionne.

Fichiers conseilles :

```txt
exercices/05_docker/
|-- README.md
|-- notes-dyma.md
|-- commandes.md
|-- erreurs.md
|-- 01_nginx/
|-- 02_image_simple/
|-- 03_node_server/
|-- 04_postgres_volume/
|-- 05_compose_api_db/
`-- 06_prod_notes/
```

Ne cree pas tout a l'avance. Cree seulement le dossier du chapitre en cours.

## Plan Dyma adapte

| Chapitre Dyma | Exercice dans le repo | Validation |
|---|---|---|
| 1. Introduction a Docker | Ecrire `notes-dyma.md` : pourquoi Docker, image, conteneur, isolation | Tu peux expliquer Docker en 5 phrases simples |
| 2. Decouvrir les bases de Docker | Lancer `hello-world`, puis `nginx` avec un port expose | La page nginx est accessible et les logs sont lus |
| 3. Creer une image avec un Dockerfile | Creer une image simple dans `02_image_simple/` | `docker build` fonctionne et l'image apparait dans `docker images` |
| 4. Trouver et partager des images Docker | Pull une image, lire ses tags, taguer ton image locale | Tu sais expliquer `image:tag` et registry |
| 5. Image Docker pour un serveur Node | Creer une petite API Node dans `03_node_server/` | `curl http://localhost:8000/health` repond |
| 6. Persister des donnees avec Docker | Lancer PostgreSQL avec un volume dans `04_postgres_volume/` | Une donnee reste apres recreation du conteneur |
| 7. Les reseaux Docker | Connecter une API a PostgreSQL via un network | L'API utilise le nom du service ou du conteneur DB |
| 8. Utiliser Docker Compose | Creer `docker-compose.yml` API + PostgreSQL + Adminer | `docker compose up -d` lance tous les services |
| 9. Compose pour application client | Ajouter un client minimal si utile | Le client appelle l'API en local |
| 10. Compose avec plusieurs services | Finaliser une stack API + DB + Adminer ou client + API + DB | `docker compose ps` montre les services sains |
| 11. Mise en production Docker Compose | Ajouter `.env.example`, notes de prod et debug | Le README explique lancement, logs, stop, reset |
| 12. PHP et Symfony | Optionnel sauf si tu choisis Symfony | Tu sais dire pourquoi tu l'as fait ou laisse pour plus tard |

## Commandes a maitriser

```bash
docker version
docker info
docker run hello-world
docker run --name web -p 8080:80 nginx
docker ps
docker ps -a
docker logs web
docker exec -it web sh
docker stop web
docker rm web
docker images
docker build -t myapp:dev .
docker run --env-file .env -p 8000:8000 myapp:dev
docker volume ls
docker network ls
docker compose up -d
docker compose ps
docker compose logs -f
docker compose down
```

## Resultat attendu

A la fin du bloc Docker, tu dois avoir :

- une API dockerisee;
- un `Dockerfile` propre;
- un `.dockerignore`;
- un `docker-compose.yml`;
- PostgreSQL avec volume;
- un `.env.example`;
- un README avec les commandes;
- une section debug avec les erreurs rencontrees.

Phrase cible :

> J'ai suivi un parcours Docker pratique : j'ai lance des conteneurs simples, construit mes images, ajoute PostgreSQL avec un volume, connecte les services avec Compose, puis documente les commandes de lancement et de debug.
