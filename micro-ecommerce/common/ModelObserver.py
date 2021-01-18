from django.db import transaction, IntegrityError
from core.models import CheckoutItem, Checkout
from django.db.models.signals import post_save
from rest_framework import serializers
from django.dispatch import receiver
from core.models import Product

class ModelObserver:

    def __init__(self, sender, serializer=None) -> None:
        self.sender = sender
        self.serializer = serializer
    
    def register(self):
        receiver(post_save, sender=self.sender)(self.model_saved)
    
    def model_saved(self, instance, created, **kwargs):
        '''
        created received a boolean, False equals update.
        '''
        if not created and instance.status.message == "Approved Purchase":
            try:
                items = instance.checkout_items.all()
                with transaction.atomic():
                    for item in items:
                        current_product = Product.objects.get(id=str(item.product.id))
                        current_product.stock -= item.quantity
                        current_product.save()
            except IntegrityError as e:
                raise serializers.ValidationError("Error: {}".format(e))