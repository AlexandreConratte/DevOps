# FEUILLE DE ROUTE DEVOPS - 6 MOIS

Programme pense pour un debutant qui vise une alternance DevOps.

Rythme recommande :

- 5 a 8 heures par semaine minimum.
- 2 sessions courtes de theorie.
- 2 sessions de pratique.
- 1 session documentation / GitHub.

Chaque semaine doit produire quelque chose de visible : notes, script, Dockerfile, pipeline, mini-projet ou README.

---

## Vue d'ensemble

| Mois | Theme | Objectif principal | Preuve GitHub |
|---|---|---|---|
| 1 | Linux, terminal, Git, reseau | Etre a l'aise dans un environnement serveur | Notes + exercices + mini scripts |
| 2 | Bash, Python utilitaire, YAML, logs | Automatiser de petites taches | Repo "devops-toolbox" |
| 3 | Docker, Compose, PostgreSQL | Lancer une application complete en local | App dockerisee |
| 4 | CI/CD, serveur, Nginx, HTTPS | Automatiser et deployer | Pipeline + deploiement documente |
| 5 | Cloud, Terraform, monitoring, securite | Industrialiser proprement | Infra as Code + dashboard |
| 6 | Kubernetes intro + projet final | Montrer une vision DevOps complete | Projet portfolio final |

---

## Mois 1 - Fondations

### Objectif

Comprendre ce qu'est un serveur, comment s'y deplacer, comment une application parle au reseau et comment travailler avec Git.

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 1 | Role DevOps + terminal | `cd`, `ls`, `mkdir`, `touch`, `cat`, `nano`, `less` |
| 2 | Linux fichiers, droits, processus | `chmod`, `chown`, `ps`, `top`, `systemctl`, `journalctl` |
| 3 | Reseau web | IP, port, DNS, HTTP, HTTPS, firewall |
| 4 | Git / GitHub | clone, branch, commit, push, Pull Request |

### Mini-projet

Creer un repo `linux-git-basics` avec :

- un fichier `COMMANDES_LINUX.md`;
- un fichier `RESEAU_WEB.md`;
- un script `check_port.sh` qui teste si un port est ouvert;
- des commits propres par chapitre.

### Validation

L'apprenant doit pouvoir expliquer :

- ce qu'est un port;
- pourquoi une app ecoute sur `localhost:3000`;
- comment lire un log;
- ce qu'est une branche Git;
- comment revenir a un etat propre sans paniquer.

---

## Mois 2 - Automatisation simple

### Objectif

Transformer des commandes repetitives en scripts.

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 5 | Bash base | variables, conditions, boucles, codes de sortie |
| 6 | Scripts systeme | backup, check HTTP, lecture de logs |
| 7 | Python utilitaire | fichiers, JSON, requetes HTTP simples |
| 8 | YAML + logs | lire et modifier des fichiers de configuration |

### Projet portfolio 1

Repo `devops-toolbox`.

Contenu :

- `backup_folder.sh` : sauvegarde un dossier en `.tar.gz`;
- `check_website.sh` : verifie qu'un site repond;
- `log_errors.py` : lit un fichier de log et extrait les lignes `ERROR`;
- `README.md` avec exemples d'utilisation.

### Validation

L'apprenant doit pouvoir dire :

> J'ai automatise des verifications simples en Bash et Python, avec des scripts documentes et executables.

---

## Mois 3 - Docker et applications composees

### Objectif

Comprendre comment emballer une application et ses dependances.

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 9 | Docker base | image, conteneur, port, logs |
| 10 | Dockerfile | construire une image simple |
| 11 | Docker Compose | API + PostgreSQL + Adminer |
| 12 | Volumes, networks, `.env` | persister les donnees et configurer proprement |

### Projet portfolio 2

Repo `dockerized-api`.

Contenu :

- une petite API Node, Python ou Go;
- un `Dockerfile`;
- un `docker-compose.yml`;
- une base PostgreSQL;
- un `.env.example`;
- un README avec commandes de lancement.

### Validation

L'apprenant doit pouvoir expliquer :

- difference entre image et conteneur;
- pourquoi utiliser un volume pour PostgreSQL;
- pourquoi ne pas mettre de secrets dans Git;
- comment lire les logs d'un conteneur.

---

## Mois 4 - CI/CD et deploiement serveur

### Objectif

Automatiser les verifications et mettre l'application en ligne.

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 13 | GitHub Actions | lancer tests et lint au push |
| 14 | Build Docker en CI | construire une image automatiquement |
| 15 | Serveur Linux / VPS | SSH, users, firewall, Docker sur serveur |
| 16 | Nginx + HTTPS | reverse proxy, domaine, certificat TLS |

### Projet portfolio 3

Ameliorer `dockerized-api` :

- pipeline GitHub Actions;
- build Docker automatique;
- deploiement sur VPS ou plateforme cloud;
- Nginx devant l'API;
- HTTPS;
- documentation de debug.

### Validation

Phrase cible d'entretien :

> Quand je pousse mon code, GitHub Actions verifie le projet. Ensuite je peux construire l'image Docker et deployer l'application sur un serveur Linux expose via Nginx en HTTPS.

---

## Mois 5 - Cloud, Terraform, monitoring, securite

### Objectif

Passer de "ca marche" a "c'est maintenable".

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 17 | Cloud | VM, region, storage, security group, IAM |
| 18 | Terraform | init, plan, apply, state, variables |
| 19 | Monitoring | Uptime Kuma, Prometheus, Grafana |
| 20 | Securite de base | secrets, SSH keys, least privilege, Trivy |

### Mini-projet

Repo `infra-lab`.

Contenu :

- exemple Terraform local ou cloud;
- documentation sur `plan` et `apply`;
- monitoring simple d'une API;
- scan Trivy d'une image Docker;
- checklist securite.

### Validation

L'apprenant doit pouvoir expliquer :

- pourquoi l'infrastructure en code evite les clics manuels fragiles;
- ce qu'est le state Terraform;
- difference entre log, metrique et alerte;
- ce qu'il ne faut jamais committer.

---

## Mois 6 - Kubernetes et projet final

### Objectif

Comprendre Kubernetes sans essayer de devenir expert trop tot.

### Semaines

| Semaine | Sujet | A savoir faire |
|---|---|---|
| 21 | Kubernetes base | cluster, node, pod, deployment, service |
| 22 | YAML K8s | appliquer un Deployment et un Service |
| 23 | Ingress, ConfigMap, Secret | exposer et configurer une app |
| 24 | Projet final | finaliser un repo propre et racontable en entretien |

### Projet final portfolio

Repo `devops-final-project`.

Objectif :

```txt
API + PostgreSQL
-> Docker Compose en local
-> CI GitHub Actions
-> image Docker
-> deploiement serveur avec Nginx
-> monitoring simple
-> option Kubernetes local avec kind ou minikube
```

### Validation finale

L'apprenant doit avoir :

- 3 a 4 repos propres;
- des README clairs;
- des screenshots de pipeline / dashboard;
- une documentation de deploiement;
- une page "ce que j'ai appris";
- des explications simples pour entretien.

---

## Ordre a respecter

Ne pas commencer par Kubernetes.

Ordre logique :

1. Linux
2. Reseau
3. Git
4. Bash
5. Docker
6. Docker Compose
7. CI/CD
8. Deploiement serveur
9. Cloud
10. Terraform
11. Monitoring
12. Kubernetes
13. Securite continue

Pourquoi ?

Parce que Kubernetes repose sur Docker, Docker repose sur Linux, CI/CD repose sur Git, et le cloud repose sur les bases reseau.

