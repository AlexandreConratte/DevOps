# Scripts

Outils d'automatisation crees pendant la Mission 2.

## check_http.py

Verifie qu'une URL HTTP repond avec le code attendu.

```bash
python3 scripts/check_http.py http://localhost:8000/health
python3 scripts/check_http.py --timeout 2 --expect 200 http://localhost:8000/health
```

Codes de sortie :

- `0` : endpoint OK.
- `2` : endpoint indisponible ou code HTTP inattendu.

## check_disk.py

Verifie l'utilisation disque d'un chemin.

```bash
python3 scripts/check_disk.py /mnt/c --warning 70 --critical 90
python3 scripts/check_disk.py /mnt/c --warning 0 --critical 90
python3 scripts/check_disk.py /mnt/c --warning 0 --critical 0
```

Codes de sortie :

- `0` : disque sous le seuil warning.
- `1` : disque au-dessus ou egal au seuil warning.
- `2` : disque au-dessus ou egal au seuil critical.
- `3` : configuration de seuils invalide.

## backup_dir.sh

Cree une archive `.tar.gz` d'un dossier source vers un dossier destination, puis ecrit un log dans `logs/backup.log`.

```bash
bash scripts/backup_dir.sh signe-de-vie backups
bash scripts/backup_dir.sh dossier-inexistant backups
tail -n 5 logs/backup.log
```

Codes de sortie :

- `0` : backup cree.
- `2` : erreur d'usage, source absente, ou creation d'archive impossible.
