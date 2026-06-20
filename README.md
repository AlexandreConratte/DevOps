# Programme DevOps Projet-First

Objectif : accompagner une personne débutante jusqu'à un niveau crédible pour viser un stage ou une alternance DevOps junior en France.

Le livrable final n'est pas une pile de notes. C'est un GitHub présentable : un projet fil rouge déployé, documenté, observable, automatisé, avec des preuves concrètes à montrer en entretien.

## Point De Départ

On apprend en construisant.

Chaque chapitre est une mission : tu pars d'un brief, tu construis, tu bloques, tu lis l'encadré de cours utile, puis tu continues. La théorie sert le projet, pas l'inverse.

## Ce Que Tu Construis

Le fil rouge est un backend de chatbot en Python, FastAPI et PostgreSQL.

Il grandit mission après mission :

```txt
FastAPI + PostgreSQL
-> Docker Compose
-> CI/CD
-> image publiée
-> VPS + Nginx + HTTPS
-> logs + monitoring + incident
-> LLM externe + Cloud Run
-> Terraform + CD
-> Kubernetes optionnel
-> vitrine GitHub recruteur-ready
```

À côté du fil rouge, quelques missions produisent de petits repos satellites utiles : journal DevOps, serveur public minimal, scripts d'automatisation.

## Comment Utiliser Ce Repo

1. Ouvre [PARCOURS.md](./PARCOURS.md) pour voir les missions et les paliers.
2. Travaille une mission à la fois depuis `missions/*/MISSION.md`.
3. Committe à chaque étape importante avec un message clair.
4. Dépose les preuves dans `flagship/evidence/` quand la mission le demande.
5. Utilise `ressources/` comme aide-mémoire : commandes, debug, glossaire, prompts IA, portfolio.
6. Après la Mission 6, commence à postuler en parallèle de la suite.

## Paliers

| Palier | Missions | Résultat |
| --- | --- | --- |
| Employable Core | 0 à 6 | App dockerisée, testée, en ligne, monitorée, avec sauvegarde et runbook |
| Cloud / IaC Plus | 7 à 8 | Cloud Run, LLM externe, Terraform, CD, budget cloud maîtrisé |
| Wow Optionnel | 9 | Kubernetes local, HPA, Kustomize, test de charge optionnel |
| Vitrine | 10 | README, preuves, schéma, CV, pitch, profil GitHub |

## Structure

```txt
.
├── README.md
├── PARCOURS.md
├── PLAN_REFONTE.md
├── agent.md
├── missions/
├── flagship/
│   ├── app/
│   ├── migrations/
│   ├── ansible/
│   ├── k8s/
│   └── evidence/
└── ressources/
```

## Règle D'or

Ne dis pas seulement : "je connais Docker, Terraform, Grafana".

Dis plutôt :

> J'ai pris une API FastAPI avec PostgreSQL, je l'ai conteneurisée, testée en CI, publiée en image Docker, déployée en HTTPS sur un VPS, surveillée avec Prometheus/Grafana, puis j'ai documenté un incident et les preuves d'exploitation.

Un profil junior crédible ne prétend pas tout savoir. Il montre qu'il sait construire, vérifier, documenter, débugger et expliquer.

## IA Dans Le Parcours

L'IA est utilisée comme accélérateur : aide au debug, relecture de config, génération de première version, amélioration de README, préparation d'entretien.

Elle n'est jamais la source de vérité. Chaque suggestion doit être confirmée par des tests, la CI, des logs, des métriques, des scans ou une commande de diagnostic.

La trace utile de cette pratique est conservée dans [ressources/AI_USAGE_LOG.md](./ressources/AI_USAGE_LOG.md) et, quand c'est pertinent, dans `flagship/evidence/`.
