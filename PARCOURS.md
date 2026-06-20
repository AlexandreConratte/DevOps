# Parcours DevOps Projet-First

Ce fichier est la carte du parcours. Les détails vivent dans chaque `missions/*/MISSION.md`.

## Vision

On construit d'abord. On lit seulement quand un blocage rend la théorie utile.

Chaque mission doit laisser trois traces :

- un changement concret dans un repo ;
- une preuve vérifiable dans `flagship/evidence/` quand c'est pertinent ;
- une phrase d'entretien que l'apprenant peut défendre.

## Vue D'ensemble

| # | Mission | Résultat | Statut |
| --- | --- | --- | --- |
| 0 | Boot | Environnement de dev + premier repo propre | Obligatoire |
| 1 | Signe de vie | Serveur HTTP public qui survit à un reboot | Obligatoire |
| 2 | La Forge | Scripts Bash/Python utiles + cron + logs | Obligatoire |
| 3 | Mise en boîte | Backend chatbot FastAPI + PostgreSQL + Docker Compose + Alembic | Obligatoire |
| 4 | Le Gardien | CI GitHub Actions + scans + image GHCR | Obligatoire |
| 5 | Grande Ouverture | Déploiement VPS + Nginx + HTTPS + Ansible + backup/restore | Obligatoire |
| 6 | Tour de Contrôle | Monitoring, logs, incident simulé, runbook, postmortem | Obligatoire |
| 7 | Le Cerveau | LLM externe + Cloud Run + secrets + coûts + résilience | Conseillé |
| 8 | L'Architecte | Terraform GCP + CD + preuve de coût/teardown | Conseillé |
| 9 | Sous Pression | Kubernetes local + Kustomize + HPA, boss cloud optionnel | Optionnel |
| 10 | Vitrine | Portfolio GitHub, README, captures, pitch, CV | Obligatoire |

## Paliers

### Employable Core

Missions 0 à 6.

À la fin de ce palier, l'apprenant peut commencer à candidater. Il a déjà une application conteneurisée, testée, déployée, monitorée et documentée.

### Cloud / IaC Plus

Missions 7 et 8.

Ce palier montre une pratique moderne : cloud serverless, secrets, budget, Terraform, CD.

### Wow Optionnel

Mission 9.

Kubernetes ne doit pas bloquer la fin du parcours. Le core local suffit pour un junior ; le boss cloud est un bonus court, borné et destructible.

### Vitrine

Mission 10.

Cette mission est obligatoire. Elle transforme le travail technique en preuve lisible pour un recruteur.

## Cadence Suggérée

| Mois | Missions | Jalon |
| --- | --- | --- |
| 1 | 0, 1 | Environnement prêt + serveur public minimal |
| 2 | 2, 3 | Scripts utiles + naissance du chatbot dockerisé |
| 3 | 4, 5 | CI, image, VPS, HTTPS, Ansible, backup |
| 4 | 6 | Monitoring, incident, postmortem, candidature possible |
| 5 | 7, 8 | LLM externe, Cloud Run, Terraform, CD |
| 6 | 9, 10 | Kubernetes optionnel + portfolio final |

On avance à la Definition of Done, pas au calendrier.

## Règles De Travail

- Une mission à la fois.
- Un commit par étape racontable.
- Une preuve quand un service fonctionne.
- Une note de debug quand quelque chose casse.
- Un usage IA utile par moment fort, avec validation humaine.
- Aucun secret dans Git.
- Tout ce qui coûte de l'argent doit avoir une checklist de teardown.

## Coût

Le parcours vise un budget très limité.

- VPS : coût récurrent assumé, environ 5 euros par mois selon l'hébergeur.
- Domaine : facultatif au début, recommandé pour la Mission 5.
- GCP : free tier et crédits nouveaux comptes à vérifier au moment de créer le compte.
- Kubernetes cloud : optionnel, session courte, teardown obligatoire.

## Après La Mission 6

L'apprenant peut commencer à postuler avec un pitch simple :

> J'ai construit un backend FastAPI avec PostgreSQL, je l'ai conteneurisé, testé en CI, publié en image Docker, déployé en HTTPS sur un VPS, surveillé avec Grafana/Prometheus et documenté un incident.

Les missions suivantes renforcent le profil, mais ne doivent pas repousser indéfiniment les candidatures.
