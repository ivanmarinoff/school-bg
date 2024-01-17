#!/bin/sh

echo "Install the dependencies"
pip install --upgrade pip
#pip install -r requirements.txt


echo "Running Database Migrations"
python manage.py createcachetable
python manage.py makemigrations
python manage.py migrate

echo "Running app commands"
python manage.py collectstatic --noinput -c
python manage.py runserver 0.0.0.0:8000
exec "$@"