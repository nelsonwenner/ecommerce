from django.db.models.signals import post_save
from django.dispatch import receiver

class ModelObserver:

    def __init__(self, sender) -> None:
        self.sender =  sender

    def register(self):
        receiver(post_save, sender=self.sender)(self.model_saved)
    
    def model_saved(self, instance, created, **kwargs):
        
        

    