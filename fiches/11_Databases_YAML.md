# BASES DE DONNEES ET YAML - FICHE DEVOPS

## En bref

Beaucoup d'applications utilisent une base de donnees.

Un DevOps doit comprendre comment l'application s'y connecte, comment garder les donnees et comment sauvegarder.

YAML est le format de configuration de nombreux outils DevOps.

## Image mentale

La base de donnees est le coffre ou l'application range ses informations.

YAML est une fiche de consignes lisible par les humains et par les outils.

Si le coffre disparait, les donnees disparaissent.

Si la fiche YAML est mal indentee, l'outil ne comprend plus les consignes.

## Bases de donnees courantes

| Outil | Version simple |
|---|---|
| PostgreSQL | Base relationnelle tres frequente |
| MySQL | Autre base relationnelle tres connue |
| Redis | Stockage rapide en memoire |
| SQLite | Petite base dans un fichier |

## Mots importants

| Mot | Version simple |
|---|---|
| Table | Liste structuree de donnees |
| Backup | Sauvegarde |
| Restore | Restauration |
| Migration | Changement de structure de base |
| Volume Docker | Stockage persistant pour garder les donnees |
| Connection string | URL de connexion a la base |

## Exemple URL PostgreSQL

```txt
postgres://user:password@localhost:5432/app
```

Lecture :

| Partie | Sens |
|---|---|
| `postgres` | Type de base |
| `user` | Nom utilisateur |
| `password` | Mot de passe |
| `localhost` | Adresse du serveur |
| `5432` | Port PostgreSQL |
| `app` | Nom de la base |

## PostgreSQL avec Docker Compose

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  pgdata:
```

Le volume `pgdata` garde les donnees.

## Backup simple

```bash
docker exec db pg_dump -U app app > backup.sql
```

Restore simple :

```bash
docker exec -i db psql -U app app < backup.sql
```

Selon le nom du conteneur, il faut remplacer `db`.

## YAML

YAML est utilise par :

- Docker Compose;
- GitHub Actions;
- GitLab CI;
- Kubernetes;
- Ansible;
- Helm.

Exemple :

```yaml
app:
  name: demo
  port: 8000
  debug: false
```

Point important :

> YAML depend fortement de l'indentation.

Mauvais :

```yaml
app:
name: demo
```

Bon :

```yaml
app:
  name: demo
```

## Erreurs classiques YAML

| Erreur | Consequence |
|---|---|
| Mauvaise indentation | Config invalide ou mauvaise interpretation |
| Tabs au lieu d'espaces | Probleme de parsing |
| Guillemets oublies dans certains cas | Valeur mal comprise |
| Copie-colle sans verifier | Pipeline ou deploy casse |

## Niveau attendu en alternance

Tu dois savoir :

- lancer PostgreSQL avec Docker;
- comprendre une URL de connexion;
- expliquer pourquoi un volume est important;
- faire un backup simple;
- lire un YAML;
- corriger une indentation YAML simple.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | URL DB | Decoupe une URL PostgreSQL | Chaque partie expliquee |
| Facile | YAML | Corrige une indentation cassee | YAML valide |
| Facile | Compose DB | Lis un service PostgreSQL Compose | Tu identifies image/env/volume |
| Moyen | Volume | Supprime/recree un conteneur sans perdre la DB | Donnees conservees |
| Moyen | Backup | Fais un `pg_dump` simple | Fichier cree |
| Dur | Restore | Restaure un backup dans une base vide | Donnees visibles |

## Drill - 5 questions

1. Pourquoi une application a souvent besoin d'une base ?
2. A quoi sert un volume Docker pour PostgreSQL ?
3. C'est quoi une migration ?
4. Pourquoi YAML est fragile avec l'indentation ?
5. Difference entre backup et restore ?

Validation : minimum 4/5.

## A retenir

Un DevOps junior doit comprendre que les donnees sont precieuses.

On peut recreer un conteneur.

On ne peut pas toujours recreer des donnees perdues.
