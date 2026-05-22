# MONITORING, LOGS ET SECURITE DE BASE - FICHE DEVOPS

## En bref

Deployer une application ne suffit pas.

Il faut savoir si elle fonctionne, comprendre ce qui casse et eviter les erreurs dangereuses.

Monitoring = tableau de bord.

Logs = journal des evenements.

Securite = reduire les risques.

## Image mentale

Une application en production est comme une voiture sur la route.

Tu as besoin :

- du compteur de vitesse;
- du voyant moteur;
- du niveau d'essence;
- d'un carnet d'entretien;
- de freins en bon etat.

Sans monitoring et logs, tu conduis les yeux fermes.

## Logs

Un log raconte ce qui s'est passe.

Exemples :

```txt
INFO Server started on port 8000
WARNING Disk usage above 80%
ERROR Database connection failed
```

Niveaux courants :

| Niveau | Sens |
|---|---|
| DEBUG | Detail utile en developpement |
| INFO | Evenement normal |
| WARNING | Probleme potentiel |
| ERROR | Erreur qui demande attention |
| CRITICAL | Probleme grave |

Commandes utiles :

```bash
docker logs api
docker logs -f api
journalctl -u nginx
journalctl -u nginx --since "1 hour ago"
```

## Monitoring

Le monitoring mesure la sante du systeme.

On surveille souvent :

- disponibilite;
- CPU;
- RAM;
- disque;
- temps de reponse;
- nombre de requetes;
- taux d'erreur;
- etat de la base de donnees.

Outils :

| Outil | Usage |
|---|---|
| Uptime Kuma | Verifie qu'un site repond |
| Prometheus | Collecte des metriques |
| Grafana | Affiche les dashboards |
| Loki | Centralise les logs |
| Alertmanager | Envoie des alertes |
| Trivy | Scanne les images Docker |

## Difference log, metrique, alerte

| Element | Question |
|---|---|
| Log | Que s'est-il passe exactement ? |
| Metrique | Combien ? A quelle vitesse ? |
| Alerte | Faut-il prevenir quelqu'un ? |

## Securite de base

Regles a garder :

- ne jamais mettre de mot de passe dans Git;
- utiliser `.env` pour les secrets locaux;
- fournir `.env.example` sans vrais secrets;
- utiliser des cles SSH;
- limiter les ports ouverts;
- donner le minimum de droits necessaire;
- mettre a jour les dependances;
- scanner les images Docker;
- utiliser HTTPS.

## Exemple `.env.example`

```txt
DATABASE_URL=postgres://user:password@db:5432/app
API_PORT=8000
LOG_LEVEL=info
```

Ce fichier montre les variables attendues, mais ne contient pas les vrais secrets de production.

## Niveau attendu en alternance

Tu dois savoir :

- lire des logs;
- chercher une erreur;
- expliquer INFO/WARNING/ERROR;
- expliquer une metrique;
- expliquer une alerte;
- proteger les secrets;
- comprendre least privilege;
- lancer un scan simple d'image Docker.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Logs | Classe 10 lignes en INFO/WARNING/ERROR | Classement juste |
| Facile | Secret | Cree `.env.example` propre | Aucun vrai secret |
| Facile | Checklist | Ecris 8 regles securite de base | Regles concretes |
| Moyen | Uptime | Surveille une URL avec Uptime Kuma | Check actif |
| Moyen | Incident | Simule une app down et note la procedure | Procedure claire |
| Dur | Trivy | Scanne une image Docker | Resultat explique |

## Drill - 5 questions

1. Difference entre log et metrique ?
2. Pourquoi monitorer une application ?
3. Que signifie `ERROR` dans un log ?
4. Pourquoi ne jamais committer un secret ?
5. C'est quoi le principe du moindre privilege ?

Validation : minimum 4/5.

## A retenir

Un DevOps ne se contente pas de deployer.

Il rend le systeme observable, debuggable et moins fragile.

