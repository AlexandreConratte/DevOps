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
python3 scripts/check_disk.py /mnt/c --critical 80
python3 scripts/check_disk.py /mnt/c --critical 0
```

Codes de sortie :

- `0` : disque sous le seuil critique.
- `2` : disque au-dessus ou egal au seuil critique.
