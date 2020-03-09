#!/bin/bash
set -e

./manage.py create_admin_superuser
./manage.py migrate --noinput
