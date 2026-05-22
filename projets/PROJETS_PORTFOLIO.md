# PROJETS PORTFOLIO DEVOPS

Objectif : construire des projets simples mais credibles pour chercher une alternance DevOps.

Un bon projet DevOps n'est pas forcement une application compliquee.

Un bon projet DevOps montre que tu sais rendre une application plus fiable, plus automatisable et plus facile a deployer.

---

## Projet 1 - DevOps Toolbox

### But

Creer une boite a outils de scripts utiles.

### Stack

- Bash
- Python
- Linux
- GitHub

### Fonctionnalites

| Script | Role |
|---|---|
| `backup_folder.sh` | Compresse un dossier avec date dans le nom |
| `check_website.sh` | Verifie qu'une URL repond |
| `check_disk.sh` | Alerte si le disque depasse un seuil |
| `extract_errors.py` | Extrait les lignes `ERROR` d'un fichier de log |
| `json_report.py` | Lit un JSON et genere un resume |

### README attendu

Le README doit contenir :

- objectif du projet;
- prerequis;
- commandes d'installation;
- exemples d'utilisation;
- problemes rencontres;
- pistes d'amelioration.

### Ce que ca montre

Tu sais automatiser des taches simples et documenter proprement.

---

## Projet 2 - Dockerized API

### But

Dockeriser une petite API avec base PostgreSQL.

### Stack

- API Python FastAPI, Node Express ou autre stack simple;
- Docker;
- Docker Compose;
- PostgreSQL;
- Adminer ou pgAdmin;
- `.env.example`.

### Fonctionnalites minimales

- endpoint `GET /health`;
- endpoint `GET /items`;
- endpoint `POST /items`;
- connexion PostgreSQL;
- donnees persistantes via volume Docker.

### Fichiers attendus

```txt
.
|-- Dockerfile
|-- docker-compose.yml
|-- .env.example
|-- README.md
|-- app/
`-- scripts/
```

### README attendu

Inclure :

- comment lancer en local;
- comment arreter;
- comment lire les logs;
- comment reset la base;
- schema simple de l'architecture.

### Ce que ca montre

Tu sais emballer une application et lancer plusieurs services ensemble.

---

## Projet 3 - CI/CD Pipeline

### But

Ajouter une pipeline GitHub Actions au projet Docker.

### Stack

- GitHub Actions;
- tests;
- lint;
- build Docker;
- secrets GitHub.

### Pipeline minimale

Au push :

1. installer les dependances;
2. lancer les tests;
3. verifier le format;
4. construire l'image Docker.

### Bonus

- push de l'image vers GitHub Container Registry;
- badge de statut dans le README;
- separation `main` / Pull Request.

### Ce que ca montre

Tu sais automatiser les controles de qualite avant de deployer.

---

## Projet 4 - Deploiement VPS avec Nginx

### But

Deployer l'API dockerisee sur un serveur Linux.

### Stack

- VPS ou VM cloud;
- SSH;
- Docker;
- Docker Compose;
- Nginx;
- HTTPS avec Let's Encrypt;
- firewall.

### Etapes attendues

1. creer un utilisateur non-root;
2. configurer SSH;
3. installer Docker;
4. copier ou pull le projet;
5. lancer `docker compose up -d`;
6. configurer Nginx en reverse proxy;
7. activer HTTPS;
8. documenter comment deboguer.

### Ce que ca montre

Tu sais passer de "ca marche en local" a "c'est en ligne".

---

## Projet 5 - Monitoring simple

### But

Surveiller que l'application repond et comprendre les logs.

### Stack

- Uptime Kuma;
- Docker Compose;
- logs applicatifs;
- option Grafana/Prometheus.

### Fonctionnalites

- monitorer `/health`;
- simuler une panne;
- documenter ou l'alerte apparait;
- ecrire une mini procedure d'incident.

### Procedure d'incident attendue

```txt
1. Verifier si l'URL repond.
2. Lire les logs Nginx.
3. Lire les logs Docker.
4. Verifier l'etat des conteneurs.
5. Relancer le service si besoin.
6. Ecrire ce qui s'est passe.
```

### Ce que ca montre

Tu sais surveiller une application et reagir de facon methodique.

---

## Projet final - DevOps Final Project

### But

Assembler les briques principales dans un seul repo portfolio.

### Architecture cible

```txt
Utilisateur
-> HTTPS
-> Nginx
-> API Docker
-> PostgreSQL Docker volume
-> Monitoring /health
```

### Livrables

- API fonctionnelle;
- Dockerfile;
- Docker Compose;
- GitHub Actions;
- deploiement serveur documente;
- monitoring simple;
- securite de base;
- README complet;
- schema d'architecture;
- section "ce que j'ai appris".

### Bonus

- Terraform pour creer la VM;
- Kubernetes local avec kind ou minikube;
- scan Trivy;
- dashboard Grafana.

### Pitch entretien

> J'ai construit une petite API, je l'ai dockerisee avec PostgreSQL, j'ai ajoute une pipeline CI/CD, je l'ai deployee sur un serveur Linux derriere Nginx avec HTTPS, puis j'ai ajoute un monitoring simple et une documentation de debug.
