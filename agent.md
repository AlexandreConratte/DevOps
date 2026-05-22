# Agent Guide

## Objectif du repo

Ce repo contient un programme d'apprentissage DevOps progressif, concu pour partir des bases et construire des competences pratiques jusqu'a un niveau credible pour une alternance junior.

Le but est de transformer des notions DevOps en parcours concret :

```txt
comprendre les concepts
-> pratiquer avec des exercices
-> construire des mini-projets
-> realiser des projets portfolio
-> savoir expliquer son travail en entretien
```

## Public cible

Le contenu vise un profil debutant.

Chaque notion doit donc etre expliquee simplement, avec :

- une idee centrale claire;
- une analogie concrete;
- des mots importants definis;
- des exemples pratiques;
- des exercices progressifs;
- un drill de validation.

## Style attendu

Les fiches doivent rester pedagogiques, directes et vulgarisees.

Eviter :

- le jargon non explique;
- les longs blocs de theorie sans pratique;
- les listes d'outils sans contexte;
- les explications trop expertes trop tot.

Preferer :

- des phrases courtes;
- des tableaux lisibles;
- des commandes utiles;
- des exemples proches du terrain;
- des validations mesurables.

## Progression pedagogique

Respecter l'ordre logique :

1. Linux
2. Reseau
3. Git
4. Bash / Python
5. YAML / bases de donnees simples
6. Docker
7. Docker Compose
8. CI/CD
9. Deploiement serveur
10. Monitoring / logs / securite
11. Cloud
12. Terraform
13. Kubernetes

Ne pas introduire Kubernetes, Terraform ou Grafana avant que les bases Linux, reseau, Git, YAML, bases de donnees simples et Docker soient posees.

Ne pas introduire Docker Compose avance ou CI/CD avant que l'apprenant comprenne les bases de YAML, des variables d'environnement et d'une connexion PostgreSQL.

## Regle pratique

Chaque fiche doit aider a produire quelque chose :

- une commande testee;
- un script;
- un fichier de configuration;
- un Dockerfile;
- une pipeline;
- une procedure de debug;
- une documentation;
- un projet GitHub presentable.

Une fiche purement theorique doit rester l'exception.

## Objectif final

A la fin du parcours, le repo doit permettre de construire et raconter ce type de projet :

```txt
API simple
-> Dockerfile
-> Docker Compose avec PostgreSQL
-> pipeline GitHub Actions
-> deploiement sur serveur Linux
-> Nginx + HTTPS
-> logs et monitoring simple
-> securite de base
-> documentation claire
```

Le resultat attendu n'est pas l'expertise senior.

Le resultat attendu est une base junior solide, pratique, documentee et montrable.

