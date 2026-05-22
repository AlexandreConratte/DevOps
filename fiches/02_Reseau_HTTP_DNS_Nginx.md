# RESEAU, HTTP, DNS ET NGINX - FICHE DEVOPS

## En bref

Le reseau permet aux machines de communiquer.

Une application web fonctionne parce qu'un navigateur trouve un serveur, se connecte a un port, puis envoie une requete HTTP ou HTTPS.

## Image mentale

Imagine un immeuble.

- L'adresse IP = adresse de l'immeuble.
- Le port = numero de porte dans l'immeuble.
- DNS = annuaire qui transforme un nom en adresse.
- HTTP = langue parlee entre navigateur et serveur.
- HTTPS = meme langue, mais chiffree.
- Nginx = receptionniste qui oriente les visiteurs.

## Les mots importants

| Mot | Version simple |
|---|---|
| IP | Adresse d'une machine sur un reseau |
| Port | Porte d'entree vers un service |
| DNS | Traduit un nom de domaine en IP |
| HTTP | Protocole des sites web |
| HTTPS | HTTP chiffre avec TLS |
| TCP | Communication fiable entre machines |
| Firewall | Filtre ce qui peut entrer ou sortir |
| Reverse proxy | Serveur qui recoit puis redirige les requetes |
| Nginx | Outil frequent pour servir ou rediriger du trafic web |

## Ce qui se passe quand tu ouvres un site

Exemple :

```txt
https://mon-site.com
```

Chemin simplifie :

```txt
mon-site.com
-> DNS trouve l'IP
-> navigateur contacte l'IP sur le port 443
-> Nginx recoit la requete
-> Nginx transmet a l'application
-> l'application repond
```

## Ports frequents

| Port | Usage |
|---:|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 3000 | App web en dev |
| 8000 | API en dev |

## Commandes utiles

```bash
curl http://localhost:8000/health
curl -I https://example.com
ping example.com
nslookup example.com
lsof -i :8000
```

Selon le systeme, `dig` peut remplacer `nslookup`.

## Nginx en reverse proxy

Une app peut tourner sur le serveur en local :

```txt
localhost:8000
```

Mais les utilisateurs vont sur :

```txt
https://api.monsite.com
```

Nginx fait le lien :

```nginx
server {
    listen 80;
    server_name api.monsite.com;

    location / {
        proxy_pass http://localhost:8000;
    }
}
```

Version simple :

> Quand quelqu'un arrive sur `api.monsite.com`, Nginx transmet a l'application qui tourne sur `localhost:8000`.

## Pourquoi un site peut etre inaccessible

Ca peut venir de :

- DNS mal configure;
- serveur eteint;
- firewall qui bloque;
- mauvais port;
- Nginx mal configure;
- application arretee;
- certificat HTTPS expire;
- base de donnees inaccessible.

## Niveau attendu en alternance

Tu dois comprendre :

- ce qu'est une IP;
- ce qu'est un port;
- pourquoi HTTP et HTTPS sont differents;
- pourquoi DNS est utile;
- le role d'un firewall;
- le role de Nginx;
- comment tester une URL avec `curl`.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Ports | Liste 5 ports connus et leur role | Les roles sont justes |
| Facile | Curl | Fais `curl -I https://example.com` | Tu expliques le status code |
| Facile | DNS | Trouve l'IP d'un domaine avec `nslookup` | Tu comprends le resultat |
| Moyen | Port local | Lance une app locale puis retrouve son port avec `lsof` | Tu identifies le processus |
| Moyen | Schema | Dessine le trajet `DNS -> IP -> Nginx -> app` | Schema clair |
| Dur | Debug | Ecris une checklist "mon site ne repond pas" | Minimum 8 causes possibles |

## Drill - 5 questions

1. Quelle difference entre IP et DNS ?
2. A quoi sert un port ?
3. Pourquoi HTTPS est plus sur que HTTP ?
4. C'est quoi un reverse proxy ?
5. Pourquoi Nginx est souvent place devant une application ?

Validation : minimum 4/5.

## A retenir

Le reseau, c'est le chemin entre l'utilisateur et l'application.

Un DevOps junior doit savoir suivre ce chemin et trouver ou ca bloque.

