#!/bin/sh

# Run database migrations
echo "Running migrations..."
python manage.py migrate

# Start the server
echo "Starting server..."
exec "$@"
