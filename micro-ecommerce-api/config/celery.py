from celery import Celery, bootsteps
from django.db import transaction
from celery import Celery
import kombu
import os

#------------------------------------------------------#
#                 PRODUCER SETTINGS                    #
#------------------------------------------------------#

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('celery_app')

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

def _publish(message, routing_key):
    with rabbitmq_producer() as producer:
        producer.publish(
            body=message,
            routing_key=routing_key,
            exchange='checkout'
        )

#------------------------------------------------------#
#                 CONSUMER WORKER                      #
#------------------------------------------------------#

with rabbitmq_conn() as conn:
    queue = kombu.Queue(
        name='queue-checkout',
        exchange='checkout',
        routing_key='payment',
        channel=conn,
        durable=True
    )
    queue.declare()

class PaymentConsumer(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [
            kombu.Consumer(
                channel,
                queues=[queue],
                callbacks=[self.handle_message],
                accept=['json']
            )
        ]

    def handle_message(self, data, message):
        from payment_gateway.proccess_payment import proccess_payment_simulation
        from core.models import Checkout
        
        try:

            result = proccess_payment_simulation(
                card_hash=data['card_hash'],
                payment_method=data['payment_method']
            )

            with transaction.atomic():
                checkout = Checkout.objects.get(id=str(data['checkout_id']))
                checkout.status_id = "e2182812-d1b0-4585-99bf-6510497602ab"
                checkout.remote_id = result
                checkout.save()

        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)

        message.ack()

app.steps['consumer'].add(PaymentConsumer)