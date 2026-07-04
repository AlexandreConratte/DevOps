# Mission 2 - Check disk

Statut : script d'automatisation valide en local WSL.

## Contexte

Un script Python verifie l'utilisation disque d'un chemin et retourne un code de sortie exploitable.

Script :

```text
scripts/check_disk.py
```

Documentation :

```text
scripts/README.md
```

## Commandes

Cas OK :

```bash
cd /mnt/c/Users/conra/devOps
python3 scripts/check_disk.py /mnt/c --critical 80
echo $?
```

Cas critique force :

```bash
python3 scripts/check_disk.py /mnt/c --critical 0
echo $?
```

Aide :

```bash
python3 scripts/check_disk.py --help
```

## Resultats observes

Cas OK :

```text
OK path=/mnt/c used_pct=... free_gb=...
0
```

Cas critique :

```text
CRITICAL path=/mnt/c used_pct=... free_gb=...
2
```

## Points valides

- Chemin configurable avec l'argument `path`.
- Seuil configurable avec `--critical`.
- Arguments documentes avec `--help`.
- Code de sortie `0` en cas OK.
- Code de sortie `2` en cas critique.
