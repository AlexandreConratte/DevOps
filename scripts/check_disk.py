#!/usr/bin/env python3
import argparse
import shutil
import sys


# argparse lit les arguments passes dans la commande.
parser = argparse.ArgumentParser(description="Check disk usage for a path.")
parser.add_argument("path", help="Path to check, for example /")  # argument obligatoire
parser.add_argument(
    "--critical",
    type=float,
    default=80,
    help="Critical threshold in percent. Default: 80",
)
parser.add_argument(
    "--warning",
    type=float,
    default=70,
    help="Warning threshold in percent. Default: 70",
)

# parse_args stocke les valeurs dans args.path, args.warning et args.critical.
args = parser.parse_args()

# disk_usage retourne total, used et free en octets.
usage = shutil.disk_usage(args.path)

# Convertit les valeurs pour obtenir un pourcentage et des Go lisibles.
used_pct = usage.used / usage.total * 100
free_gb = usage.free / 1024 / 1024 / 1024

# Une configuration avec warning >= critical n'a pas de sens.
if args.warning >= args.critical:
    print(" Warning threshold must be lower than Critical threshold", file=sys.stderr)
    sys.exit(3)

# On teste CRITICAL avant WARNING, car un disque critique depasse aussi le seuil warning.
if used_pct >= args.critical:
    print(
        f"CRITICAL path={args.path} used_pct={used_pct:.2f} "  # :.2f affiche deux chiffres apres la virgule.
        f"free_gb={free_gb:.1f}",
        file=sys.stderr,
    )
    sys.exit(2)


if used_pct >= args.warning:
    print(
        f"WARNING path={args.path} used_pct={used_pct:.2f} " 
        f"free_gb={free_gb:.1f}",
        file=sys.stderr,
    )
    sys.exit(1)

print(f"OK path={args.path} used_pct={used_pct:.2f} free_gb={free_gb:.1f}")
sys.exit(0)
