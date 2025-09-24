#!/usr/bin/env bash
set -euo pipefail
URL="${1:?usage: smoke.sh <url>}"
TRIES="${2:-20}"
DELAY="${3:-3}"
echo "Smoke testing $URL ..."
for i in $(seq 1 "$TRIES"); do
  if curl -sfL "$URL" >/dev/null; then
    echo "OK"
    curl -s "$URL"
    exit 0
  fi
  echo "retry $i/$TRIES ..."
  sleep "$DELAY"
done
echo "Smoke test failed for $URL" >&2
exit 1
