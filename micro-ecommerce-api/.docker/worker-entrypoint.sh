#!/bin/bash

cd /home/django/app

pip install -r requirements.txt

dockerize -wait tcp://database:5432 -wait tcp://app:8000 -timeout 2700s -wait-retry-interval 10s

celery worker -B -l info -A config.celery -s /tmp/celerybeat-schedule
