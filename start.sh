#!/bin/bash
python -m pip install --upgrade pip
pip install virtualenv
virtualenv /opt/venv
source /opt/venv/bin/activate
pip install --no-cache-dir -r requirements.txt
python manage.py migrate
gunicorn DemoMultitenant.wsgi --workers 2 --timeout 120 --bind 0.0.0.0:$PORT