# TP 01 - Linux, terminal et SSH

Objectif : transformer la fiche Linux en pratique concrete.

Ce TP doit etre fait dans un terminal Linux. Si tu es sous Windows, utilise de preference WSL Ubuntu. PowerShell peut aider pour Git, mais ce n'est pas le terminal cible de cette fiche.

## Resultat attendu

A la fin du TP, tu dois avoir produit :

- un dossier de travail `devops/linux/lab`;
- un fichier `notes.txt`;
- un script executable `hello.sh`;
- un faux fichier de logs `app.log`;
- une procedure `procedure_debug.md`;
- une trace des commandes, erreurs et reponses dans le README ou dans un fichier `reponses.md`.

## Duree conseillee

Prevoir 1h30 a 2h.

Ne cherche pas a aller vite. Le but est de comprendre ce que chaque commande fait.

## Regles du TP

- Lance les commandes toi-meme.
- Note les commandes importantes.
- Note au moins une erreur rencontree, meme petite.
- Ne passe pas a la partie suivante si tu ne comprends pas le resultat observe.
- A la fin, refais les etapes principales sans copier-coller.

---

## Partie 0 - Preparation

### Objectif

Verifier ou tu es dans le terminal et creer un espace de travail.

### Commandes

```bash
pwd
mkdir -p devops/linux/lab
cd devops/linux/lab
pwd
ls -la
```

### Resultat attendu

- `pwd` affiche un chemin qui se termine par `devops/linux/lab`.
- `ls -la` affiche le contenu du dossier, meme s'il est presque vide.

### A noter

```md
## Partie 0 - Preparation

Commandes lancees :

Resultat observe :

Erreur ou question :
```

---

## Partie 1 - Navigation et fichiers

### Objectif

Savoir creer un fichier, lister un dossier et comprendre ou on se trouve.

### Commandes

```bash
touch notes.txt
ls
ls -la
pwd
```

Ajoute ensuite 5 lignes dans `notes.txt`.

Tu peux utiliser un editeur :

```bash
nano notes.txt
```

Ou des commandes simples :

```bash
echo "Linux est souvent utilise sur les serveurs." > notes.txt
echo "Le terminal permet de commander la machine." >> notes.txt
echo "pwd affiche le dossier courant." >> notes.txt
echo "ls liste les fichiers." >> notes.txt
echo "cd permet de changer de dossier." >> notes.txt
```

### Resultat attendu

- `notes.txt` existe.
- Le fichier contient 5 lignes.
- Tu sais expliquer la difference entre `>` et `>>`.

### Verification

```bash
cat notes.txt
wc -l notes.txt
```

---

## Partie 2 - Lire un fichier

### Objectif

Comprendre la difference entre afficher tout un fichier, son debut et sa fin.

### Commandes

```bash
cat notes.txt
head notes.txt
tail notes.txt
head -n 2 notes.txt
tail -n 2 notes.txt
```

### Resultat attendu

- `cat` affiche tout le fichier.
- `head` affiche le debut.
- `tail` affiche la fin.
- `-n 2` limite l'affichage a 2 lignes.

### A ecrire dans ta restitution

Explique avec tes mots :

```md
cat sert a :
head sert a :
tail sert a :
```

---

## Partie 3 - Droits et script executable

### Objectif

Comprendre pourquoi un script doit avoir le droit d'execution.

### Creation du script

Cree un fichier `hello.sh`.

```bash
nano hello.sh
```

Contenu a mettre dans le fichier :

```bash
#!/usr/bin/env bash
echo "Bonjour depuis Linux"
echo "Dossier courant : $(pwd)"
```

### Verification des droits

```bash
ls -l hello.sh
```

Essaie de lancer le script avant de le rendre executable :

```bash
./hello.sh
```

Il est possible que tu obtiennes une erreur de permission. C'est normal.

### Rendre le script executable

```bash
chmod +x hello.sh
ls -l hello.sh
./hello.sh
```

### Resultat attendu

- `ls -l` montre un `x` dans les droits du fichier.
- `./hello.sh` affiche le message du script.

### A noter

```md
Erreur observee avant chmod +x :

Difference observee apres chmod +x :

Ce que signifie le droit x :
```

---

## Partie 4 - Processus et PID

### Objectif

Comprendre qu'un programme en cours d'execution devient un processus, identifie par un PID.

### Lancer une commande longue

```bash
sleep 300 &
echo $!
```

La commande `sleep 300 &` lance un processus en arriere-plan. La commande `echo $!` affiche le PID du dernier processus lance en arriere-plan.

### Retrouver le processus

```bash
ps aux | grep sleep
```

### Arreter le processus

Remplace `<PID>` par le numero que tu as observe.

```bash
kill <PID>
ps aux | grep sleep
```

### Resultat attendu

- Tu retrouves une ligne contenant `sleep 300`.
- Tu identifies son PID.
- Apres `kill`, le processus ne doit plus etre actif.

### A noter

```md
PID observe :

Commande utilisee pour retrouver le processus :

Commande utilisee pour l'arreter :
```

---

## Partie 5 - Logs avec tail -f

### Objectif

Comprendre comment suivre un fichier de logs en direct.

### Terminal 1

Dans un premier terminal :

```bash
touch app.log
tail -f app.log
```

La commande reste ouverte. C'est normal.

### Terminal 2

Ouvre un deuxieme terminal, retourne dans le meme dossier, puis ajoute des lignes :

```bash
cd <CHEMIN_DU_LAB>
echo "$(date) INFO application started" >> app.log
echo "$(date) INFO request GET /health" >> app.log
echo "$(date) ERROR database unavailable" >> app.log
```

Remplace `<CHEMIN_DU_LAB>` par le chemin affiche par `pwd` dans la partie 0.

### Retour au terminal 1

Tu dois voir les nouvelles lignes apparaitre en direct.

Pour quitter `tail -f`, utilise :

```txt
Ctrl+C
```

### Resultat attendu

- `tail -f` affiche les lignes ajoutees sans relancer la commande.
- Tu sais expliquer pourquoi les logs sont utiles pour deboguer une application.

---

## Partie 6 - Systeme, disque et memoire

### Objectif

Connaitre quelques commandes de diagnostic de base.

### Commandes

```bash
df -h
free -h
top
```

Dans `top`, quitte avec :

```txt
q
```

### Resultat attendu

- `df -h` montre l'espace disque.
- `free -h` montre la memoire.
- `top` montre les processus actifs et la consommation CPU/RAM.

### A noter

```md
Commande pour verifier le disque :

Commande pour verifier la memoire :

Commande pour surveiller les processus :
```

---

## Partie 7 - Services et logs systeme

### Objectif

Decouvrir `systemctl` et `journalctl`, qui servent souvent sur un serveur Linux.

Cette partie peut ne pas fonctionner dans tous les environnements, notamment certains WSL. Si une commande echoue, note l'erreur : c'est une bonne trace d'apprentissage.

### Commandes

```bash
systemctl --version
systemctl status ssh
journalctl -n 20
```

Si `ssh` n'existe pas comme service, essaie seulement de comprendre l'erreur.

### Resultat attendu

- Sur un vrai Linux avec systemd, `systemctl` affiche l'etat d'un service.
- `journalctl` affiche des logs systeme.
- Si la commande ne fonctionne pas, tu sais noter proprement l'erreur.

### A noter

```md
systemctl fonctionne dans mon environnement : oui/non

Erreur observee si ca ne fonctionne pas :

Ce que j'ai compris sur les services :
```

---

## Partie 8 - SSH

### Objectif

Comprendre le role de SSH sans forcement avoir encore un vrai serveur distant.

### A lire

SSH sert a se connecter de maniere securisee a une machine distante, par exemple un VPS Linux.

Commandes typiques :

```bash
ssh user@192.0.2.10
ssh -i ~/.ssh/devops-key.pem user@192.0.2.10
chmod 600 ~/.ssh/devops-key.pem
```

Ne lance pas ces commandes si tu n'as pas de serveur ou de cle SSH. L'adresse `192.0.2.10` est une adresse d'exemple.

### A ecrire

Dans ta restitution, explique :

```md
SSH sert a :

La commande ssh user@ip signifie :

La commande chmod 600 sur une cle privee sert a :
```

---

## Partie 9 - Mini-simulation d'incident

### Objectif

Ecrire une procedure simple de debug : "mon application ne repond plus".

Cree un fichier :

```bash
nano procedure_debug.md
```

Dedans, ecris une procedure en 6 etapes minimum.

Exemple de structure :

```md
# Procedure de debug - Application qui ne repond plus

1. Verifier que je suis sur la bonne machine.
2. Verifier les processus actifs.
3. Lire les derniers logs applicatifs.
4. Verifier l'espace disque.
5. Verifier l'etat du service web.
6. Noter l'erreur exacte avant de modifier quoi que ce soit.
```

Ameliore cette procedure avec les commandes que tu as apprises.

---

## Partie 10 - Restitution finale

### Objectif

Transformer ton TP en preuve visible.

Complete le README du dossier ou cree un fichier `reponses.md`.

Format conseille :

````md
# TP Linux - Restitution

## Ce que j'ai fait

- ...

## Commandes utilisees

```txt
...
```

## Resultats observes

- ...

## Erreurs rencontrees

- ...

## Comment j'ai debogue

- ...

## Ce que j'ai compris

- ...

## Drill

1. A quoi sert `pwd` ?
2. Quelle difference entre `cat`, `head` et `tail` ?
3. Pourquoi rendre un script executable ?
4. Qu'est-ce qu'un PID ?
5. A quoi sert SSH ?
````

---

## Checklist de validation

Avant de considerer le TP termine, verifie :

- [ ] Je sais aller dans `devops/linux/lab`.
- [ ] J'ai cree `notes.txt`.
- [ ] J'ai lu `notes.txt` avec `cat`, `head` et `tail`.
- [ ] J'ai cree `hello.sh`.
- [ ] J'ai rendu `hello.sh` executable avec `chmod +x`.
- [ ] J'ai lance `./hello.sh`.
- [ ] J'ai lance un processus long avec `sleep 300 &`.
- [ ] J'ai retrouve son PID.
- [ ] J'ai arrete le processus avec `kill`.
- [ ] J'ai suivi `app.log` avec `tail -f`.
- [ ] J'ai teste `df -h`, `free -h` et `top`.
- [ ] J'ai compris a quoi servent `systemctl`, `journalctl` et SSH.
- [ ] J'ai ecrit `procedure_debug.md`.
- [ ] J'ai rempli une restitution.
- [ ] J'ai note au moins une erreur ou question.

## Validation avant de passer a la suite

Tu peux passer a la fiche suivante si tu peux expliquer simplement :

- ce qu'est un dossier courant;
- pourquoi `ls -la` est plus detaille que `ls`;
- pourquoi un script doit etre executable;
- ce qu'est un PID;
- pourquoi les logs sont utiles;
- a quoi sert SSH;
- quoi verifier en premier quand une application ne repond plus.
