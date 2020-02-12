#!/bin/bash
set -e

./manage.py collectstatic --noinput
./manage.py migrate --noinput
