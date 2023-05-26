celery -A TrucksSearch.celery beat -l info &
celery -A TrucksSearch.celery worker -l info