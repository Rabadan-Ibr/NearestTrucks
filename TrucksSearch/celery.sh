celery -A config.celery beat -l info &
celery -A config.celery worker -l info