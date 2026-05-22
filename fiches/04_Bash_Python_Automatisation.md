# BASH, PYTHON ET AUTOMATISATION - FICHE DEVOPS

## En bref

Le DevOps automatise les taches repetitives.

Bash est pratique pour enchainer des commandes systeme.

Python est pratique pour traiter des fichiers, du JSON, des API et des rapports.

## Image mentale

Faire 10 commandes a la main, c'est comme laver 10 assiettes une par une.

Ecrire un script, c'est construire un petit lave-vaisselle pour refaire la meme action sans effort.

## Bash ou Python ?

| Besoin | Outil conseille |
|---|---|
| Lancer des commandes Linux | Bash |
| Deplacer/copier des fichiers | Bash |
| Verifier si une URL repond | Bash ou Python |
| Lire du JSON | Python |
| Appeler une API | Python |
| Generer un rapport | Python |
| Automatisation tres courte | Bash |
| Logique plus complexe | Python |

## Bash minimum

```bash
#!/bin/bash

set -e

URL="http://localhost:8000/health"

echo "Verification de $URL"

if curl -fsS "$URL" > /dev/null; then
  echo "OK: application disponible"
else
  echo "ERROR: application indisponible"
  exit 1
fi
```

Points importants :

- `#!/bin/bash` indique comment executer le script;
- `set -e` arrete le script si une commande echoue;
- `exit 1` signale une erreur.

## Python minimum

```python
from pathlib import Path

log_file = Path("app.log")

for line in log_file.read_text().splitlines():
    if "ERROR" in line:
        print(line)
```

Python est plus lisible des que la logique grandit.

## Codes de sortie

Un script peut finir avec un code :

| Code | Sens |
|---:|---|
| 0 | Succes |
| autre que 0 | Erreur |

La CI/CD utilise beaucoup cette logique.

Si les tests finissent avec `exit 1`, la pipeline echoue.

## Niveau attendu en alternance

Tu dois savoir ecrire des scripts pour :

- sauvegarder un dossier;
- verifier une URL;
- lire un fichier de log;
- lancer plusieurs commandes;
- retourner un code d'erreur propre;
- documenter comment utiliser le script.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Hello script | Cree `hello.sh` qui affiche un message | Executable avec `./hello.sh` |
| Facile | Backup | Script qui compresse un dossier | Archive creee |
| Facile | Variables | Script qui prend un nom en argument | Affichage correct |
| Moyen | Check HTTP | Script qui teste une URL avec `curl` | Code 0 si OK, 1 sinon |
| Moyen | Logs Python | Script Python qui extrait les lignes `ERROR` | Sortie correcte |
| Dur | Rapport | Python lit un log et compte INFO/WARNING/ERROR | Rapport lisible |

## Drill - 5 questions

1. Pourquoi automatiser une tache ?
2. Quand choisir Bash plutot que Python ?
3. A quoi sert `chmod +x` ?
4. Que signifie un code de sortie `0` ?
5. Pourquoi la CI/CD aime les scripts qui echouent proprement ?

Validation : minimum 4/5.

## A retenir

Un DevOps junior n'a pas besoin d'ecrire des scripts enormes.

Il doit surtout savoir automatiser proprement les petites actions repetitives.

