# DEPLOIEMENT, CLOUD, NGINX ET HTTPS - FICHE DEVOPS

## En bref

Deployer, c'est mettre une application en ligne sur une machine accessible par les utilisateurs.

Le cloud permet de louer cette machine au lieu d'acheter un serveur physique.

Nginx recoit le trafic web et le transmet a l'application.

HTTPS chiffre les echanges.

## Image mentale

Ton application est une boutique.

- Le serveur = local commercial.
- Le cloud = proprietaire qui te loue le local.
- Le DNS = annuaire avec l'adresse.
- Nginx = reception.
- HTTPS = conversation dans une piece fermee plutot qu'en public.

## Les mots importants

| Mot | Version simple |
|---|---|
| VM | Serveur virtuel loue dans le cloud |
| Region | Zone geographique ou tourne le serveur |
| Provider | Fournisseur cloud : AWS, Azure, GCP, OVH, Scaleway |
| IAM | Gestion des utilisateurs et permissions |
| Security group | Firewall cote cloud |
| Load balancer | Repartit le trafic entre plusieurs serveurs |
| Reverse proxy | Transmet les requetes vers le bon service |
| TLS | Technologie derriere HTTPS |

## Deploiement simple sur VPS

Chemin typique :

```txt
1. Acheter ou creer un VPS
2. Se connecter en SSH
3. Creer un utilisateur deploy
4. Installer Docker
5. Copier le projet ou faire git clone
6. Lancer docker compose up -d
7. Configurer Nginx
8. Ajouter HTTPS
9. Surveiller les logs
```

## Commandes utiles

```bash
ssh deploy@ip_du_serveur
sudo apt update
sudo ufw status
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
docker compose up -d
docker compose ps
docker compose logs -f
sudo systemctl status nginx
sudo nginx -t
sudo systemctl reload nginx
```

## Exemple Nginx reverse proxy

```nginx
server {
    listen 80;
    server_name api.monsite.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Version simple :

> Nginx recoit `api.monsite.com` et transmet a l'API locale sur le port 8000.

## HTTPS avec Let's Encrypt

Let's Encrypt donne des certificats gratuits.

Outil courant :

```bash
sudo certbot --nginx -d api.monsite.com
```

Le certificat permet au navigateur d'afficher le cadenas HTTPS.

## Checklist securite minimale serveur

- SSH avec cle, pas mot de passe si possible;
- utilisateur non-root pour deployer;
- firewall actif;
- ports ouverts seulement si necessaire;
- secrets dans `.env`, jamais dans Git;
- mises a jour regulieres;
- logs consultables;
- backups si donnees importantes.

## Niveau attendu en alternance

Tu dois comprendre :

- ce qu'est une VM;
- comment se connecter en SSH;
- pourquoi ouvrir seulement certains ports;
- comment lancer une app Docker sur serveur;
- comment Nginx expose l'app;
- pourquoi HTTPS est necessaire.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Plan de deploiement | Ecris les etapes d'un deploy VPS | Minimum 8 etapes |
| Facile | Firewall | Explique les ports 22/80/443 | Explications justes |
| Facile | Nginx | Lis une config reverse proxy | Tu identifies `proxy_pass` |
| Moyen | Serveur local | Simule Nginx devant une app locale | Requete transmise |
| Moyen | Procedure | Ecris "comment rollback" | Procedure claire |
| Dur | Deploy reel | Deploy une API sur VPS | URL publique fonctionnelle |

## Drill - 5 questions

1. C'est quoi une VM ?
2. Pourquoi utiliser SSH ?
3. Pourquoi mettre Nginx devant une API ?
4. A quoi sert HTTPS ?
5. Pourquoi limiter les ports ouverts ?

Validation : minimum 4/5.

## A retenir

Deployer, ce n'est pas juste "mettre en ligne".

C'est rendre l'application accessible, securisee, observable et redemarrable.

