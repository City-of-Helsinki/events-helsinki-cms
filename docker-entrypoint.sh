#!/bin/bash

set -e


if [[ "$WAIT_FOR_IT_ADDRESS" ]]; then
    wait-for-it.sh $WAIT_FOR_IT_ADDRESS --timeout=30
fi


if [[ "$APPLY_MIGRATIONS" = "true" ]]; then
    ./manage.py migrate --noinput
fi


if [[ "$CREATE_SUPERUSER" = "true" ]]; then
    ./manage.py create_admin_superuser
fi


if [[ "$DEV_SERVER" = "true" ]]; then
    ./manage.py runserver $DEV_SERVER_ADDRESS
else
    gunicorn --config gunicorn_configurations.py project.wsgi
fi
