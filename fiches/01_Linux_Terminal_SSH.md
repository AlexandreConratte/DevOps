# LINUX, TERMINAL ET SSH - FICHE DEVOPS

## En bref

Linux est le systeme le plus courant sur les serveurs.

Un DevOps doit savoir se connecter a un serveur, se deplacer dans les dossiers, lire des fichiers, verifier des processus, lire des logs et relancer des services.

## Image mentale

Le terminal, c'est comme piloter une machine avec des instructions courtes.

Au lieu de cliquer dans une interface, tu dis directement :

```bash
va dans ce dossier
liste les fichiers
affiche ce log
relance ce service
```

## Pourquoi c'est important

Une application de production tourne souvent sur une machine Linux.

Quand ca casse, il faut pouvoir repondre vite :

- est-ce que le service tourne ?
- est-ce que le disque est plein ?
- est-ce qu'il y a une erreur dans les logs ?
- est-ce que les droits du fichier sont bons ?
- est-ce que je peux me connecter en SSH ?

## Les mots importants

| Mot | Version simple |
|---|---|
| Terminal | Interface pour commander la machine avec du texte |
| Shell | Programme qui comprend tes commandes |
| Fichier | Element qui contient des donnees |
| Dossier | Boite qui contient des fichiers ou d'autres dossiers |
| Permission | Droit de lire, modifier ou executer |
| Processus | Programme en train de tourner |
| Service | Programme gere par le systeme en arriere-plan |
| Log | Journal de ce qui s'est passe |
| SSH | Connexion securisee a une machine distante |

## Commandes essentielles

### Se deplacer

| Commande | Role |
|---|---|
| `pwd` | Affiche le dossier actuel |
| `ls` | Liste les fichiers |
| `ls -la` | Liste avec details et fichiers caches |
| `cd dossier` | Va dans un dossier |
| `cd ..` | Remonte d'un niveau |
| `mkdir app` | Cree un dossier |
| `touch fichier.txt` | Cree un fichier vide |

### Lire des fichiers

| Commande | Role |
|---|---|
| `cat fichier` | Affiche tout le fichier |
| `less fichier` | Lit un gros fichier page par page |
| `head fichier` | Affiche le debut |
| `tail fichier` | Affiche la fin |
| `tail -f fichier` | Suit un fichier en direct |

### Droits

| Commande | Role |
|---|---|
| `chmod +x script.sh` | Rend un script executable |
| `chmod 600 key.pem` | Protege une cle privee SSH |
| `chown user fichier` | Change le proprietaire |

### Processus et services

| Commande | Role |
|---|---|
| `ps aux` | Liste les processus |
| `top` | Surveille CPU/RAM |
| `systemctl status nginx` | Etat du service Nginx |
| `systemctl restart nginx` | Relance Nginx |
| `journalctl -u nginx` | Logs du service Nginx |

### SSH

```bash
ssh user@ip_du_serveur
ssh -i cle.pem user@ip_du_serveur
```

## Exemple concret

Tu as deploye une API, mais le site ne repond plus.

Ordre de debug simple :

```bash
ssh deploy@serveur
docker ps
docker logs api
systemctl status nginx
journalctl -u nginx --since "10 minutes ago"
df -h
```

Tu verifies :

- conteneur actif;
- logs applicatifs;
- Nginx actif;
- logs systeme;
- espace disque.

## Niveau attendu en alternance

Tu dois savoir :

- te connecter en SSH;
- naviguer dans les dossiers;
- lire un fichier de config;
- modifier un fichier simple;
- comprendre les droits de base;
- lire des logs;
- verifier un service;
- relancer un service.

## Exercices

| Niveau | Exercice | Instructions | Validation |
|---|---|---|---|
| Facile | Navigation | Cree `devops/linux/lab`, entre dedans, cree `notes.txt` | Tu sais refaire sans aide |
| Facile | Lecture | Ecris 5 lignes dans `notes.txt`, lis avec `cat`, `head`, `tail` | Tu expliques la difference |
| Facile | Droits | Cree `hello.sh`, rends-le executable | `./hello.sh` fonctionne |
| Moyen | Processus | Lance une commande longue puis retrouve-la avec `ps` | Tu identifies le PID |
| Moyen | Logs | Cree un faux fichier `app.log`, suis-le avec `tail -f` | Tu observes les nouvelles lignes |
| Dur | Simulation serveur | Ecris une procedure "mon app ne repond plus" | Procedure en 6 etapes minimum |

## Drill - 5 questions

1. A quoi sert `pwd` ?
2. Quelle difference entre `cat` et `less` ?
3. Pourquoi une cle SSH privee doit-elle etre protegee ?
4. C'est quoi un processus ?
5. Pourquoi les logs sont-ils souvent la premiere chose a regarder ?

Validation : minimum 4/5.

## A retenir

Linux est la base du DevOps.

Tu n'as pas besoin de connaitre toutes les commandes.

Tu dois surtout savoir chercher, lire, verifier et deboguer calmement.

