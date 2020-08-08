#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fake_data
python manage.py loaddata initial_data
python manage.py runserver 0.0.0.0:8000