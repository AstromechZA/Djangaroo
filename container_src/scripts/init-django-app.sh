#!/bin/bash

set -ex

echo 'Initialising django app..'

cd /django_app
source /django_app/overrides.env

DJANGO_SETTINGS_MODULE=example_project.settings

python manage.py migrate
python manage.py collectstatic --noinput

supervisorctl -c /etc/supervisord.conf start django-app-run
supervisorctl -c /etc/supervisord.conf start nginx

echo 'Done'
