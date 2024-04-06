#!/bin/bash -e

if [ "$1" = 'createsuperuser' ]; then
    exec echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell

elif [ "$1" = 'run' ]; then
    ./manage.py migrate
    ./manage.py collectstatic --noinput
    exec gunicorn project.wsgi --workers=2 --bind=0.0.0.0:8000

else
    exec "${@}"

fi
