import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testcoins.settings')

app = Celery('testcoins')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

app.conf.update(
    broker_url='amqp://guest:guest@localhost:5672//',
    broker_connection_retry_on_startup=True,
    beat_scheduler='django_celery_beat.schedulers:DatabaseScheduler',
)