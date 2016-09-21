#!/bin/bash

set -eu

echo 'Starting django-app..'

cd /django_app
source /django_app/overrides.env

DJANGO_SETTINGS_MODULE=example_project.settings

ACCESS_LOG=/var/log/gunicorn-access.log
ERROR_LOG=/var/log/gunicorn-error.log

# The WSGI module that starts the process.
DJANGO_WSGI_MODULE='example_project.wsgi'

echo "gunicorn starting with DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name django_app \
  --workers 3 \
  --max-requests 1000 \
  --bind unix:/tmp/django_app.sock
