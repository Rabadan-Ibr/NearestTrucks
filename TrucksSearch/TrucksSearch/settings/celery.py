
CELERY_BEAT_SCHEDULE = {
    'update_trucks_locations': {
        'task': 'trucks.tasks.update_locations',
        'schedule': 180,
    }
}

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
