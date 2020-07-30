from common.models import AutoCreateUpdatedMixin
from django.db import models
from enum import Enum

class PaymentMethodEnum(Enum):
    CREDIT_CARD = 'credit_card'
    BANK_SLIP = 'bank_slip'

payment_method_choices = [(pm.value, pm.name) for pm in PaymentMethodEnum]

class PaymentMethod(AutoCreateUpdatedMixin):
    PAYMENT_METHOD_CHOICES = (
        ("credit_card", "credit_card"),
        ("bank_slip", "billet")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES, verbose_name='name')
    allow_installments = models.BooleanField(default=True, verbose_name='with installments')

    class Meta:
        verbose_name = 'payment method'

    def __str__(self):
        return self.get_name_display()
    
