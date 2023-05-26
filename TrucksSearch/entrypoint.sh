#!/bin/sh

python manage.py migrate

python manage.py init_locations

python manage.py init_trucks

python manage.py runserver 0.0.0.0:8000