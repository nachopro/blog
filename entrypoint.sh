#!/bin/bash

export DJANGO_SETTINGS_MODULE=settings.prod

./manage.py migrate
./manage.py runserver 0.0.0.0:8000
#gunicorn project.wsgi --workers=2 --bind=0.0.0.0:8000
