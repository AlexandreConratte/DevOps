# Mission 2 - Backup dir

Statut : script Bash de backup valide en local WSL.

## Contexte

Un script Bash cree une archive `.tar.gz` d'un dossier source et ecrit une ligne datee dans `logs/backup.log`.

Script :

```text
scripts/backup_dir.sh
```

Documentation :

```text
scripts/README.md
```

## Commandes

Cas OK :

```bash
cd /mnt/c/Users/conra/devOps
bash scripts/backup_dir.sh signe-de-vie backups
echo $?
```

Cas erreur :

```bash
bash scripts/backup_dir.sh dossier-inexistant backups
echo $?
```

Verification des logs :

```bash
tail -n 5 logs/backup.log
```

## Resultats observes

Cas OK :

```text
OK backup_created source=signe-de-vie archive=backups/backup-...
0
```

Cas erreur :

```text
CRITICAL source_dir_not_found path=dossier-inexistant
2
```

Log :

```text
2026-... OK backup_created source=signe-de-vie archive=backups/backup-...
2026-... CRITICAL source_dir_not_found path=dossier-inexistant
```

## Points valides

- Source et destination passees en arguments.
- Verification du nombre d'arguments.
- Verification que la source existe.
- Creation automatique du dossier destination.
- Archive timestamped en `.tar.gz`.
- Logs dates dans `logs/backup.log`.
- Code de sortie `0` en cas OK.
- Code de sortie `2` en cas erreur.
