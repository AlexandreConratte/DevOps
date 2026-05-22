# ROLE DEVOPS, MENTALITE ET ENTRETIEN - FICHE DEVOPS

## En bref

DevOps n'est pas seulement un metier d'outils.

C'est une facon de rendre le chemin entre le code et la production plus automatique, plus fiable, plus securise et plus facile a comprendre.

## Image mentale

Une equipe developpe une application.

Le DevOps aide a construire la route entre :

```txt
code sur l'ordinateur
-> tests automatiques
-> image Docker
-> serveur
-> deploiement
-> monitoring
-> correction en cas de probleme
```

Son travail est de rendre cette route moins fragile.

## Ce que fait un DevOps

| Sujet | Version simple |
|---|---|
| Automatisation | Eviter les actions manuelles repetitives |
| Deploiement | Mettre une application en ligne |
| Infrastructure | Gerer serveurs, cloud, reseau, conteneurs |
| CI/CD | Automatiser tests, builds et deploiements |
| Monitoring | Surveiller que tout fonctionne |
| Logs | Comprendre ce qui s'est passe |
| Securite | Proteger acces, secrets et serveurs |
| Collaboration | Faire le lien entre developpement et exploitation |
| Documentation | Rendre le travail reutilisable par l'equipe |

## Mentalite DevOps

Phrase a garder :

> Je cherche a rendre les systemes plus simples, plus fiables, plus automatises et plus faciles a maintenir.

Concretement :

- automatiser ce qui est repete;
- documenter ce qui est important;
- surveiller ce qui peut casser;
- securiser ce qui est sensible;
- standardiser ce qui doit etre refait;
- ameliorer petit a petit.

## Ce qu'on attend d'un alternant

On ne demande pas un expert.

On attend plutot :

- des bases solides;
- des manipulations concretes;
- des projets GitHub propres;
- une capacite a expliquer simplement;
- une bonne methode de debug;
- l'habitude de documenter;
- l'envie d'apprendre.

Phrase cible :

> Je ne connais pas encore tout, mais j'ai deja dockerise une application, cree une pipeline CI/CD, deploye sur un serveur Linux et documente mes etapes.

## Priorite des outils

### Priorite 1 - Indispensable

| Outil | Pourquoi |
|---|---|
| Linux | Base des serveurs |
| Git | Travail collaboratif |
| Bash | Automatisation simple |
| Docker | Conteneurisation |
| Docker Compose | Plusieurs services ensemble |
| GitHub Actions | CI/CD accessible |
| Nginx | Exposer une application |

### Priorite 2 - Tres important

| Outil | Pourquoi |
|---|---|
| Cloud provider | Heberger des applications |
| Terraform | Infrastructure as Code |
| PostgreSQL | Base de donnees frequente |
| Prometheus/Grafana | Monitoring |
| Kubernetes | Orchestration de conteneurs |

### Priorite 3 - Bonus utile

| Outil | Pourquoi |
|---|---|
| Ansible | Automatisation de configuration |
| Helm | Packaging Kubernetes |
| Loki | Logs centralises |
| Trivy | Scan securite Docker |
| Vault | Gestion avancee des secrets |
| Argo CD | GitOps |

## Reponses simples d'entretien

### DevOps

DevOps est une approche qui rapproche developpement et exploitation pour livrer plus souvent, plus vite et avec moins d'erreurs.

### Docker

Docker emballe une application avec son environnement pour qu'elle fonctionne pareil sur plusieurs machines.

### CI/CD

La CI/CD automatise les etapes entre le code et le deploiement : tests, verification, build et parfois mise en production.

### Kubernetes

Kubernetes gere automatiquement des conteneurs : il les lance, les surveille, les redemarre et aide a les exposer.

### Terraform

Terraform permet de creer et modifier de l'infrastructure avec du code au lieu de cliquer manuellement.

### Monitoring

Le monitoring surveille la sante d'une application avec des metriques, des logs et des alertes.

### Nginx

Nginx peut servir de reverse proxy : il recoit les requetes web et les transmet au bon service.

## Pieges a eviter en entretien

| Mauvaise reponse | Meilleure reponse |
|---|---|
| "Je connais Kubernetes" | "J'ai deploye une app simple en local avec un Deployment et un Service" |
| "Je sais Docker" | "J'ai cree un Dockerfile et un Compose avec API + PostgreSQL" |
| "Je suis bon en cloud" | "Je sais creer une VM, configurer SSH et ouvrir les ports necessaires" |
| "Je connais CI/CD" | "J'ai une pipeline qui lance les tests et build une image Docker" |
| "Je fais de la securite" | "Je ne commit pas les secrets, j'utilise `.env.example`, SSH keys et firewall" |

## Mini pitch personnel

Modele a adapter :

> Je suis en train de me former au DevOps avec une approche tres pratique. J'ai commence par Linux, Git et le reseau, puis j'ai dockerise une API avec PostgreSQL. J'ai ajoute une pipeline GitHub Actions pour automatiser les tests et le build Docker. Ensuite, j'ai deploye l'application sur un serveur Linux derriere Nginx avec HTTPS. Mon objectif est de continuer a progresser sur Terraform, le monitoring et Kubernetes en gardant des projets documentes sur GitHub.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Definition | Explique DevOps en 3 phrases | Clair pour un non-tech |
| Facile | Priorites | Classe 10 outils par priorite | Classement coherent |
| Facile | Pitch | Ecris ton pitch en 8 lignes | Pitch concret |
| Moyen | Projet raconte | Explique un projet Docker en entretien | Outils + probleme + resultat |
| Moyen | Debug raconte | Raconte une panne simulee | Methode claire |
| Dur | Entretien blanc | Reponds a 15 questions DevOps | Reponses simples et honnetes |

## Drill - 5 questions

1. Quel est le but principal d'une approche DevOps ?
2. Pourquoi un alternant DevOps doit-il documenter ?
3. Quels sont les outils a apprendre en priorite ?
4. Comment parler de Docker sans survendre son niveau ?
5. Quelle phrase resume la mentalite DevOps ?

Validation : minimum 4/5.

## A retenir

Un bon junior DevOps ne pretend pas tout savoir.

Il montre qu'il sait apprendre, manipuler, documenter et expliquer.

