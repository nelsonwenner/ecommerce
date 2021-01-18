#!/bin/bash

cd /usr/src/app

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

dockerize -wait tcp://database:5432 -wait tcp://rabbitmq:15672 -timeout 2700s -wait-retry-interval 10s

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fake_data 
python manage.py loaddata initial_data 
python manage.py runserver 0.0.0.0:8000
