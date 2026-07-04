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
python3 scripts/check_disk.py /mnt/c --warning 70 --critical 90
echo $?
```

Cas warning force :

```bash
python3 scripts/check_disk.py /mnt/c --warning 0 --critical 90
echo $?
```

Cas critique force :

```bash
python3 scripts/check_disk.py /mnt/c --warning 0 --critical 0
echo $?
```

Cas seuils invalides :

```bash
python3 scripts/check_disk.py /mnt/c --warning 90 --critical 80
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

Cas warning :

```text
WARNING path=/mnt/c used_pct=... free_gb=...
1
```

Cas seuils invalides :

```text
UNKNOWN warning threshold must be lower than critical threshold
3
```

## Points valides

- Chemin configurable avec l'argument `path`.
- Seuil warning configurable avec `--warning`.
- Seuil critical configurable avec `--critical`.
- Arguments documentes avec `--help`.
- Code de sortie `0` en cas OK.
- Code de sortie `1` en cas warning.
- Code de sortie `2` en cas critique.
- Code de sortie `3` en cas de configuration invalide.
