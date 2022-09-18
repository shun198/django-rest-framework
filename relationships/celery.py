import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study.settings')

app = Celery('relationships')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "no_reply_customers_task": {
        "task": "crm.tasks.no_mail_received",
        "schedule": crontab(minute=0, hour=2),
    },
    "cancel_customers_task": {
        "task": "crm.tasks.cancel_customers",
        "schedule": crontab(minute=30, hour=2),
    },
    "close_customers_task": {
        "task": "close_customers",
        "schedule": crontab(minute=0, hour=3),
    },
}