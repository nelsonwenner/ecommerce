from core.models import CheckoutItem, Checkout
from django.db.models.signals import post_save
from config.celery import rabbitmq_producer
from rest_framework import serializers
from django.dispatch import receiver
from core.models import Product

class ModelObserver:

    def __init__(self, sender, serializer=None) -> None:
        self.sender = sender
        self.serializer = serializer
    
    def register_model_saved(self):
        receiver(post_save, sender=self.sender)(self.model_saved)
    
    def model_saved(self, instance, created, **kwargs):
        pass
        
    def _publish(self, message, routing_key):
        with rabbitmq_producer() as producer:
            producer.publish(
                body=message,
                routing_key=routing_key,
                exchange='checkout'
            )