from common.models import AutoCreateUpdatedMixin
from django.db import models
from enum import Enum

class PaymentMethodEnum(Enum):
    CREDIT_CARD = 'credit_card'
    BANK_SLIP = 'bank_slip'

payment_method_choices = [(pm.value, pm.name) for pm in PaymentMethodEnum]


