# MODE D'EMPLOI DES FICHES DEVOPS

Ces fiches sont faites pour un debutant complet.

Le but n'est pas de tout memoriser.

Le but est de construire une competence visible :

```txt
Je comprends -> je manipule -> je documente -> je montre sur GitHub.
```

---

## Methode par fiche

Pour chaque fiche :

1. Lire "En bref".
2. Lire l'analogie.
3. Refaire les commandes ou manipulations.
4. Faire les exercices.
5. Repondre au drill.
6. Ecrire 5 lignes dans un journal d'apprentissage.
7. Faire un commit.

---

## Niveaux de validation

| Niveau | Definition | Exemple |
|---|---|---|
| Compris | Tu sais reformuler l'idee | "Docker emballe une app avec ses dependances" |
| Manipule | Tu as utilise l'outil | `docker compose up` fonctionne |
| Explique | Tu peux expliquer sans lire la fiche | Tu expliques image vs conteneur |
| Montre | C'est visible sur GitHub | README + code + capture si utile |

---

## Format de restitution

Pour chaque sujet travaille, creer un fichier `reponses.md` ou une section dans le README du projet.

Format conseille :

```md
# Sujet travaille

## Ce que j'ai compris

...

## Commandes utilisees

...

## Probleme rencontre

...

## Comment j'ai debogue

...

## Drill

1. ...
```

---

## Trace de progression

| Fiche | Compris | Manipule | Explique | Montre sur GitHub | Notes |
|---|---|---|---|---|---|
| 01 Linux | Non | Non | Non | Non | |
| 02 Reseau | Non | Non | Non | Non | |
| 03 Git | Non | Non | Non | Non | |
| 04 Bash/Python | Non | Non | Non | Non | |
| 05 Docker | Non | Non | Non | Non | |
| 06 CI/CD | Non | Non | Non | Non | |
| 07 Deploiement | Non | Non | Non | Non | |
| 08 Terraform | Non | Non | Non | Non | |
| 09 Kubernetes | Non | Non | Non | Non | |
| 10 Monitoring/Securite | Non | Non | Non | Non | |
| 11 Databases/YAML | Non | Non | Non | Non | |
| 12 Role/Mentalite/Entretien | Non | Non | Non | Non | |

---

## Regle anti-theorie

Une semaine sans pratique ne compte pas.

Chaque semaine doit produire au moins un de ces elements :

- un script;
- un fichier de configuration;
- un Dockerfile;
- une pipeline;
- une documentation;
- un deploiement;
- une correction de bug documentee.

---

## Comment parler en entretien

Ne pas dire :

> Je connais Docker, Kubernetes, Terraform, Grafana.

Dire plutot :

> J'ai utilise Docker pour lancer une API avec PostgreSQL, GitHub Actions pour verifier mon code, Nginx pour exposer l'application et Uptime Kuma pour surveiller qu'elle repond.

Un recruteur junior cherche surtout :

- comprehension;
- curiosite;
- rigueur;
- capacite a documenter;
- projets concrets.
