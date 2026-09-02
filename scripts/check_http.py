#!/usr/bin/env python3
import argparse
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def parse_args():
    # Prepare les arguments acceptes par la commande.
    parser = argparse.ArgumentParser(
        description="Check an HTTP endpoint and return a useful exit code."
    )
    parser.add_argument("url", help="URL to check, for example http://localhost:8000/health")
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Request timeout in seconds. Default: 5",
    )
    parser.add_argument(
        "--expect",
        type=int,
        default=200,
        help="Expected HTTP status code. Default: 200",
    )
    return parser.parse_args()


def main():
    args = parse_args()  # Lit les arguments de la commande.
    started_at = time.monotonic()
    request = Request(args.url, headers={"User-Agent": "devops-check-http/1.0"})

    try:
        with urlopen(request, timeout=args.timeout) as response:
            status = response.status
            elapsed_ms = int((time.monotonic() - started_at) * 1000)

            if status == args.expect:
                print(f"OK url={args.url} status={status} elapsed_ms={elapsed_ms}")
                return 0

            print(
                f"CRITICAL url={args.url} expected={args.expect} "
                f"status={status} elapsed_ms={elapsed_ms}",
                file=sys.stderr,
            )
            return 2
    # si le serveur repond, mais avec un code HTTP d'erreur.
    except HTTPError as error:
        elapsed_ms = int((time.monotonic() - started_at) * 1000)
        print(
            f"CRITICAL url={args.url} expected={args.expect} "
            f"status={error.code} elapsed_ms={elapsed_ms}",
            file=sys.stderr,
        )
        return 2
    # si pbm reseau : DNS, connexion refusee, serveur eteint.
    except URLError as error:
        elapsed_ms = int((time.monotonic() - started_at) * 1000)
        print(
            f"CRITICAL url={args.url} error={error.reason} elapsed_ms={elapsed_ms}",
            file=sys.stderr,
        )
        return 2
    except TimeoutError:
        elapsed_ms = int((time.monotonic() - started_at) * 1000)
        print(
            f"CRITICAL url={args.url} error=timeout elapsed_ms={elapsed_ms}",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
