# Mission 1 - Signe de vie WSL

Statut : entrainement Linux local avec WSL, ne valide pas encore la mission complete.

## Contexte

Un serveur HTTP minimal a ete lance dans Ubuntu via WSL depuis le repo local.

Repertoire :

```bash
/mnt/c/Users/conra/devOps/signe-de-vie
```

Commande de lancement :

```bash
python3 server.py
```

Commande de verification depuis Windows :

```powershell
curl.exe -i http://localhost:8000/health
```

Resultat observe :

```text
HTTP/1.1 200 OK
OK - mission 1 alive from WSL
```

## Limites

Cette preuve confirme un service HTTP minimal dans un environnement Linux local, mais il manque encore les criteres suivants de la mission complete :

- VPS accessible en SSH.
- Service HTTP joignable publiquement.
- Service gere par systemd sur un serveur.
- Redemarrage serveur teste.
