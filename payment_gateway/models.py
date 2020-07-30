from common.models import AutoCreateUpdatedMixin
from core.models import Book
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
    
class ProductPaymentMethod(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name='product')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='payment method')
    max_installments = models.SmallIntegerField(blank=True, null=True, verbose_name='maximum number of installments')
    discount_percentage = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='discount', help_text='Discount on %')
    max_installments_discount = models.SmallIntegerField(blank=True, null=True, verbose_name='parcel discount', 
    help_text='Maximum discounted parcels')

    class Meta:
        verbose_name = 'payment methods'
        unique_together = ('product_id', 'payment_method_id',)

class PaymentGateway(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='name')
    default = models.BooleanField(default=False, verbose_name='main')

    class Meta:
        verbose_name = 'payment gateway'

    def __str__(self):
        return self.name

class PaymentMethodConfig(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.ForeignKey(PaymentGateway, on_delete=models.PROTECT, verbose_name='payment method')
    max_installments = models.SmallIntegerField(blank=True, null=True,verbose_name='installment',
    help_text='If you do not allow installments, leave as 0')
    discount_percentage = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='installment',
    help_text='Discount in % (if not, leave it at 0)')

    class Meta:
        verbose_name = 'configuration of payment methods'

    def __str__(self):
        return self.payment_method.get_name_display()