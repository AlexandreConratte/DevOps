# Cheatsheet DevOps

Référence courte des commandes utiles. À compléter au fil des missions.

## Git

```bash
git status
git add .
git commit -m "message"
git push
```

## Docker

```bash
docker build -t app:local .
docker compose up -d
docker compose logs -f
docker compose down
```

## Linux

```bash
systemctl status <service>
journalctl -u <service>
ss -tulpn
curl -i http://localhost:8000/health
```
