#!/bin/bash

#Build the Project

echo "Building the Project..."
python3.8 -m pip install -r requirements.txt

echo "Making Migration"
python3.8 manage.py makemigrations --noinput
python3.8 manage.py migrate --noinput

echo "Collecting Static..."
python3.8 manage.py collectstatic --noinput --clear