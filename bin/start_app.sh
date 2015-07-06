#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn birdo.wsgi:application -b 0.0.0.0:5000 --log-level=debug --error-logfile -
