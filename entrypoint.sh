#!/bin/sh
# exit on error
set -o errexit

echo "Install the dependencies"
pip install -r requirements.txt


echo "Running Database Migrations"
python manage.py createcachetable
python manage.py migrate

echo "Running app commands"
python manage.py collectstatic --noinput
python manage.py runserver &
exec "$@"