# GIT ET GITHUB - FICHE DEVOPS

## En bref

Git garde l'historique du code.

GitHub permet de partager ce code, collaborer, ouvrir des Pull Requests et lancer des pipelines CI/CD.

## Image mentale

Git est comme une machine a sauvegarder intelligente.

Chaque commit est une photo propre du projet a un moment donne.

Une branche est une ligne parallele ou tu peux travailler sans casser la version principale.

## Les mots importants

| Mot | Version simple |
|---|---|
| Repository | Projet suivi par Git |
| Commit | Sauvegarde d'un etat du projet |
| Branch | Version parallele du projet |
| Merge | Fusion de deux branches |
| Pull Request | Proposition de changement a relire |
| Clone | Copier un repo sur sa machine |
| Push | Envoyer ses commits en ligne |
| Pull | Recuperer les changements distants |
| Conflict | Deux modifications incompatibles a resoudre |

## Commandes essentielles

```bash
git status
git add README.md
git commit -m "docs: add roadmap"
git push
git pull
git branch
git checkout -b feature/docker
git merge feature/docker
git log --oneline
```

## Workflow simple

```txt
1. Je cree une branche
2. Je modifie les fichiers
3. Je verifie git status
4. Je committe petit et clair
5. Je push
6. J'ouvre une Pull Request
7. On relit
8. On merge
```

## Messages de commit

Format simple :

```txt
type: action claire
```

Exemples :

```txt
docs: add linux notes
feat: add docker compose
fix: repair healthcheck endpoint
ci: add github actions workflow
```

## Pourquoi Git est central en DevOps

Beaucoup d'outils partent du code Git :

- GitHub Actions lit le repo pour lancer la CI;
- Docker build l'image depuis le code;
- Terraform peut etre versionne;
- Kubernetes YAML peut etre versionne;
- GitOps utilise Git comme source de verite.

## Niveau attendu en alternance

Tu dois savoir :

- cloner un projet;
- creer une branche;
- faire des commits propres;
- pousser sur GitHub;
- lire une Pull Request;
- corriger un petit conflit;
- comprendre pourquoi on ne commit pas les secrets.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Init | Cree un repo local, ajoute un README, commit | `git log` montre le commit |
| Facile | Branch | Cree `feature/notes`, modifie un fichier | Branche visible |
| Facile | Status | Fais volontairement plusieurs changements | Tu expliques `git status` |
| Moyen | Merge | Merge une branche dans `main` | Historique propre |
| Moyen | Conflit | Cree un conflit simple sur un fichier texte | Tu le resous |
| Dur | Pull Request | Ouvre une PR sur GitHub avec description | PR claire |

## Drill - 5 questions

1. C'est quoi un commit ?
2. Pourquoi travailler sur une branche ?
3. Difference entre `push` et `pull` ?
4. C'est quoi une Pull Request ?
5. Pourquoi un `.env` ne doit pas etre committe ?

Validation : minimum 4/5.

## A retenir

Git est la memoire du projet.

Un profil DevOps doit avoir un GitHub propre, lisible et documente.

