#!/usr/bin/env sh
# Give all services some time
echo 'Waiting for support services...'
sleep 5

# Wait for DB to spin up
python app/scripts/backend_pre_start.py

# Apply Alembic if needed
echo 'Alembic Upgrade'
alembic upgrade head

# Initialize Data
echo 'Initialize Data'
python app/scripts/initial_data.py

exec gunicorn -c gunicorn_conf.py app.main:app