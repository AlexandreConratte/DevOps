# Mission 1 - Signe de vie WSL systemd

Statut : entrainement systemd local avec WSL, ne valide pas encore la mission complete.

## Contexte

Le serveur HTTP minimal a ete installe comme service `systemd` dans Ubuntu via WSL.

Fichier de service source :

```text
signe-de-vie/signe-de-vie-wsl.service
```

Installation :

```bash
cd /mnt/c/Users/conra/devOps/signe-de-vie
sudo install -m 0644 signe-de-vie-wsl.service /etc/systemd/system/signe-de-vie.service
sudo systemctl daemon-reload
sudo systemctl enable --now signe-de-vie
```

Verification :

```bash
sudo systemctl status signe-de-vie --no-pager
curl -i http://localhost:8000/health
```

Resultat observe :

```text
HTTP/1.1 200 OK
OK - mission 1 alive from WSL
```

## Limites

Cette preuve confirme la gestion du service avec `systemd` dans un environnement Linux local, mais il manque encore les criteres suivants de la mission complete :

- VPS accessible en SSH.
- Service HTTP joignable publiquement.
- Redemarrage d'un serveur distant teste.
