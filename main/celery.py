"""Module-level docstring describing the purpose of the module."""


import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-expired-codes': {
        'task': 'core_apps.user.tasks.delete_expired_codes',
        'schedule': crontab(minute='*/1'),  # TODO: Change to 1 min
    },
}
