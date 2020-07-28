from django.db import models
import uuid

class AutoCreateUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class BaseCustomer(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, verbose_name='name')
    email = models.CharField(max_length=255, verbose_name='e-mail')
    personal_document = models.CharField(max_length=20, verbose_name='cpf')
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

