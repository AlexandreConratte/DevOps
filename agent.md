# Agent Guide

## Objectif Du Repo

Ce repo contient un parcours DevOps projet-first pour débutant visant un stage ou une alternance junior.

La sortie attendue est un GitHub crédible : un fil rouge FastAPI/PostgreSQL qui passe progressivement par Docker, CI/CD, VPS, HTTPS, monitoring, cloud, Terraform, IA externe et portfolio.

## Principe Pédagogique

Chaque contenu doit partir d'une mission concrète.

Ordre attendu :

```txt
brief -> action -> blocage -> cours ciblé -> preuve -> commit -> phrase d'entretien
```

La théorie doit être courte, contextualisée et placée au moment où l'apprenant en a besoin.

## Format D'une Mission

Chaque `MISSION.md` doit suivre ce squelette :

1. `🎯 Le brief`
2. `🧠 Ce que tu vas vraiment apprendre`
3. `✅ Definition of Done`
4. `🧩 Les checkpoints`
5. `📦 Plan de commits`
6. `🚀 Pour aller plus loin`
7. `🤖 IA dans cette mission`
8. `🧾 Ce que tu sais maintenant`
9. `🗣️ Ta phrase d'entretien`

Les checkpoints doivent produire des actions vérifiables, pas seulement des lectures.

## Style Attendu

Écrire pour un débutant intelligent, pas pour un expert.

Préférer :

- phrases courtes ;
- analogies simples ;
- commandes copiables ;
- erreurs classiques ;
- preuves concrètes ;
- langage d'entretien ;
- tableaux seulement quand ils clarifient.

Éviter :

- jargon non expliqué ;
- longues introductions théoriques ;
- empilement d'outils ;
- promesses trop ambitieuses ;
- contenu qui ne produit ni fichier, ni commande, ni preuve.

## IA Assistée

Chaque mission inclut un bloc `🤖 IA dans cette mission`.

Le message à faire passer :

> L'IA accélère le travail, mais la source de vérité reste la CI, les tests, les logs, les métriques, les scans et les commandes de diagnostic.

Limiter `AI_USAGE_LOG.md` à 2 ou 3 usages marquants par mission. L'objectif est de montrer une pratique saine, pas de tenir un journal exhaustif.

## Niveau Cible

Le parcours ne cherche pas à fabriquer un profil senior.

Il doit permettre à l'apprenant de dire honnêtement :

> J'ai construit, déployé, surveillé et documenté une application réelle. Je sais expliquer mes choix, retrouver une erreur, automatiser les étapes répétables et montrer des preuves de fonctionnement.
