#!/usr/bin/env python3
import shutil
import argparse
import sys


parser = argparse.ArgumentParser(description="Check disk usage for a path.")   # argparse lit les arguments passes dans la commande.
parser.add_argument("path", help="Path to check, for example /")   #déclare les arguments acceptés  ;
parser.add_argument(
      "--critical",
      type=float,
      default=80,
      help="Critical threshold in percent. Default: 80",  #lit la commande
  )
args = parser.parse_args()     #stocke le résultat dans args.path.

usage = shutil.disk_usage(args.path)     # shutil.disk_usage retourne total, used et free en octets.

used_pct = usage.used / usage.total * 100
free_gb = usage.free / 1024 / 1024 / 1024

if used_pct >= args.critical:
      print(
          f"CRITICAL path={args.path} used_pct={used_pct:.2f} "   #2f = nbr decimal type float, avec 2 chiffres après la virgule pour valeur réelle car : dans mon cas utilisation à 0,15 environ
          f"free_gb={free_gb:.1f}",
          file=sys.stderr,
      )
      sys.exit(2)

print(f"OK path={args.path} used_pct={used_pct:.2f} free_gb={free_gb:.1f}")

sys.exit(0)