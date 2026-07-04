# Mission 2 - Cron backup

Statut : cron configure en local WSL pour lancer le backup automatiquement.

## Contexte

La crontab utilisateur lance `scripts/backup_dir.sh` toutes les 5 minutes depuis le repo.

Configuration source :

```text
scripts/crontab.example
```

Ligne installee :

```cron
*/5 * * * * cd /mnt/c/Users/conra/devOps && ./scripts/backup_dir.sh signe-de-vie backups-test >> logs/cron-backup.log 2>&1
```

## Verification

Commande :

```bash
tail -n 20 logs/cron-backup.log
```

Resultat observe :

```text
backup script started
OK backup_created source=signe-de-vie archive=backups-test/backup-20260704-202001.tar.gz
```

## Points valides

- Cron installe et actif dans WSL.
- Crontab utilisateur configuree.
- Backup lance automatiquement.
- Sortie cron redirigee dans `logs/cron-backup.log`.
- Archive creee dans `backups-test/`.
