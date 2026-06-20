# Équivalences CI/CD

GitHub Actions est l'outil principal du parcours. Ce fichier aide à reconnaître les équivalents en entreprise.

| Concept | GitHub Actions | GitLab CI | Jenkins |
| --- | --- | --- | --- |
| Fichier pipeline | `.github/workflows/*.yml` | `.gitlab-ci.yml` | `Jenkinsfile` |
| Machine d'exécution | runner | runner | agent/node |
| Étape | step | script | step |
| Groupe d'étapes | job | job | stage |
| Secret | repository secret | CI/CD variable | credential |

Objectif junior : savoir lire les concepts, pas maintenir trois plateformes en profondeur.
