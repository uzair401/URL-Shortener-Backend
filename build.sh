#!/bin/bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

python manage.py collectstatic --noinput
