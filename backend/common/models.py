from django.db import models
import uuid

class AutoCreateUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class BaseCustomer(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    phone = models.CharField(max_length=12)
    personal_document = models.CharField(max_length=20, verbose_name='cpf')

    class Meta:
        abstract = True
