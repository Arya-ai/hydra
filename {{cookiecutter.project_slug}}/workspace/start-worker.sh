#!/usr/bin/env sh
# Give all services some time
echo 'Waiting for support services...'
sleep 10

# Start Celery Workers
echo 'Starting Celery Worker'
celery -A app.tasks worker -l info --autoscale=10,3