#!/bin/bash

pip install -r requirements.txt
cd /home/django/app
dockerize -wait tcp://app:8000 -timeout 10s celery worker -B -l info -A config.celery -s /tmp/celerybeat-schedule