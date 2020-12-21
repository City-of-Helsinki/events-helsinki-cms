#!/bin/bash
set -e

# Restore a DB dump
if [[ "$RESTORE_DB_DUMP" = "1" ]]; then
    echo "Restoring a database dump over the current db..."
    wormhole receive --hide-progress --accept-file --output-file /tmp/pg.sql "$RESTORE_DB_DUMP_MWH_CODE"
    psql "$DATABASE_URL" -f /tmp/pg.sql
fi

./manage.py migrate --noinput
