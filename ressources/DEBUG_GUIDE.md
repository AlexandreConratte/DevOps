# Debug Guide

Guide de diagnostic rapide. Quand quelque chose casse, on cherche des preuves avant de changer au hasard.

## Méthode

1. Décrire le symptôme en une phrase.
2. Trouver la dernière chose qui a changé.
3. Lire le message d'erreur complet.
4. Vérifier l'état du service.
5. Lire les logs.
6. Tester le chemin le plus simple.
7. Changer une seule chose à la fois.
8. Documenter la cause et la correction.

## Commandes De Base

```bash
docker ps
docker logs <container>
docker compose ps
docker compose logs -f
systemctl status <service>
journalctl -u <service> --since "30 minutes ago"
ss -tulpn
curl -i http://localhost:8000/health
```

## Questions Utiles

- Le service tourne-t-il ?
- Le port est-il ouvert ?
- Le nom DNS pointe-t-il au bon endroit ?
- Les variables d'environnement sont-elles chargées ?
- La base de données est-elle joignable ?
- Les migrations sont-elles appliquées ?
- La CI reproduit-elle le problème ?
- Les logs racontent-ils la même histoire que l'erreur visible ?
