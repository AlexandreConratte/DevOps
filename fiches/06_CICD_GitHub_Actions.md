# CI/CD ET GITHUB ACTIONS - FICHE DEVOPS

## En bref

CI/CD signifie Continuous Integration / Continuous Deployment.

Version simple :

> A chaque changement de code, une chaine automatique verifie, teste, construit et peut deployer l'application.

## Image mentale

Une pipeline CI/CD, c'est comme un tapis roulant de controle qualite.

Ton code avance et passe par plusieurs postes :

```txt
recuperer le code
-> installer
-> tester
-> verifier
-> construire
-> deployer
```

Si une etape echoue, le tapis s'arrete.

## Les mots importants

| Mot | Version simple |
|---|---|
| CI | Verifier souvent que le code s'integre bien |
| CD | Preparer ou faire le deploiement automatiquement |
| Pipeline | Suite d'etapes automatisees |
| Job | Groupe d'etapes dans une pipeline |
| Step | Une action precise |
| Runner | Machine qui execute la pipeline |
| Artifact | Fichier produit par la pipeline |
| Secret | Valeur sensible stockee hors du code |

## Pourquoi c'est important

Sans CI/CD :

- on oublie de lancer les tests;
- on build a la main;
- les deploiements dependent d'une personne;
- les erreurs arrivent plus tard.

Avec CI/CD :

- chaque push est verifie;
- les tests sont systematiques;
- le build est reproductible;
- le deploiement devient plus fiable.

## Exemple GitHub Actions simple

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

## Exemple avec build Docker

```yaml
name: Docker build

on:
  push:
    branches: ["main"]

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: docker build -t myapp:ci .
```

## Secrets

Un secret est une valeur sensible :

- mot de passe;
- token GitHub;
- cle API;
- cle SSH;
- URL de base de donnees avec credentials.

Regle :

> Jamais de secret dans le code.

Dans GitHub Actions, les secrets se lisent comme ca :

```yaml
env:
  API_TOKEN: ${{ secrets.API_TOKEN }}
```

## Niveau attendu en alternance

Tu dois savoir :

- expliquer ce qu'est une pipeline;
- lancer une pipeline au push;
- faire tourner des tests automatiquement;
- builder une image Docker en CI;
- comprendre pourquoi les secrets ne sont pas dans Git;
- lire l'erreur d'une pipeline echouee.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Workflow hello | Cree une action qui affiche `hello ci` | Action verte |
| Facile | Trigger | Lance au push et en PR | Les deux cas marchent |
| Facile | Test | Ajoute une commande de test simple | Echec si test casse |
| Moyen | Docker build | Build une image Docker en CI | Image construite |
| Moyen | Secrets | Utilise un secret factice | Valeur non visible dans Git |
| Dur | Pipeline complete | test + lint + build Docker | README avec badge |

## Drill - 5 questions

1. Que veut dire CI/CD ?
2. Pourquoi lancer les tests automatiquement ?
3. C'est quoi un runner ?
4. Pourquoi stocker les secrets dans GitHub Secrets ?
5. Que faire quand une pipeline echoue ?

Validation : minimum 4/5.

## A retenir

La CI/CD est le pont automatique entre le code et la production.

Pour un junior, une pipeline simple mais propre vaut mieux qu'une pipeline complexe mal comprise.

