# Mission 2 - Check HTTP

Statut : premier script d'automatisation valide en local WSL.

## Contexte

Un script Python verifie qu'un endpoint HTTP repond avec le code attendu et retourne un code de sortie exploitable.

Script :

```text
scripts/check_http.py
```

Documentation :

```text
scripts/README.md
```

## Commandes

Cas OK :

```bash
cd /mnt/c/Users/conra/devOps
python3 scripts/check_http.py http://localhost:8000/health
```

Cas erreur :

```bash
python3 scripts/check_http.py http://localhost:9999/health
echo $?
```

## Resultats observes

Cas OK :

```text
OK url=http://localhost:8000/health status=200 elapsed_ms=...
```

Cas erreur :

```text
CRITICAL url=http://localhost:9999/health error=... elapsed_ms=...
2
```

## Points valides

- Arguments documentes avec `--help`.
- Logs lisibles en sortie standard ou erreur.
- Code de sortie `0` en cas OK.
- Code de sortie `2` en cas critique.
