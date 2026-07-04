# Mission 1 - Signe de vie local

Statut : entrainement local, ne valide pas encore la mission complete.

## Contexte

En attendant un VPS, un serveur HTTP minimal a ete lance sur la machine locale avec PowerShell.

Commande de lancement :

```powershell
cd C:\Users\conra\devOps\signe-de-vie
powershell.exe -ExecutionPolicy Bypass -File .\server.ps1
```

Commande de verification :

```powershell
curl.exe -i http://localhost:8000/health
```

Resultat observe :

```text
HTTP/1.1 200 OK
OK - mission 1 alive
```

## Limites

Cette preuve confirme le principe d'un service HTTP minimal, mais il manque encore les criteres suivants de la mission complete :

- VPS accessible en SSH.
- Service HTTP joignable publiquement.
- Service gere par systemd.
- Redemarrage serveur teste.
