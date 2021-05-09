#!/bin/bash

cd /usr/src/app

dockerize -wait tcp://django-app:8000 -timeout 2700s -wait-retry-interval 10s

celery worker -B -l info -A config.celery -s /tmp/celerybeat-schedule
