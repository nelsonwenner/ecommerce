from django.utils.crypto import get_random_string
from celery import Celery, bootsteps
from django.db import transaction
import kombu
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('celeryapp')

'''
Using a string here means the worker doesn't have to serialize
the configuration object to child processes.
- namespace='CELERY' means all celery-related configuration keys
should have a `CELERY_` prefix.
'''
app.config_from_object('django.conf:settings', namespace='CELERY')

''' Load task modules from all registered Django app configs. '''
app.autodiscover_tasks()

''' setting publisher '''
def rabbitmq_conn():
  return app.pool.acquire(block=True)

def rabbitmq_producer():
  return app.producer_pool.acquire(block=True)

with rabbitmq_conn() as conn:
  queue = kombu.Queue(
    name='queue',
    exchange='checkout',
    routing_key='payment',
    channel=conn,
    durable=True
  )
  queue.declare()