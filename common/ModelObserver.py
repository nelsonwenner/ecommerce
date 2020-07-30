from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Book, CheckoutItem, Checkout
from django.db.models.functions import Cast
from django.db.models import TextField, UUIDField, CharField
from django.contrib.contenttypes.models import ContentType

class ModelObserver:

    def __init__(self, sender) -> None:
        self.sender =  sender

    def register(self):
        receiver(post_save, sender=self.sender)(self.model_saved)
    
    def model_saved(self, instance, created, **kwargs):
        #checkout = Checkout.objects.annotate(checkout_id=Cast('id', output_field=TextField())).values_list('checkout_id', flat=True)
        #ids = Checkout.objects.annotate(str_id=Cast('id', output_field=TextField())).values_list('str_id', flat=True)
        ids = Checkout.objects.filter(id=instance.id)
        x = [str(s) for s in ids.values_list('id', flat=True)]
        
        test = ''
        for o in x:
            for z in o:
                if z != '-':
                    test += z
            print("id1: {} id2: {} | {}".format(test , instance.id ,o == str(instance.id)))
        
        checkouts = CheckoutItem.objects.all()
        print("FIM => ", checkouts[0].id)