#!/bin/bash
echo "Running migrations..."
python manage.py migrate

# Chạy Ứng Dụng
exec "$@"
