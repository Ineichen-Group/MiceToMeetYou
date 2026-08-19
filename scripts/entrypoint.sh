#!/usr/bin/env bash
set -e

if [ -f src/manage.py ]; then
    uv run python src/manage.py migrate --noinput
    uv run python src/manage.py collectstatic --noinput --clear || true
fi

exec "$@"
