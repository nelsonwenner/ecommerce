from core.apps.payment_gateway.models import PaymentMethod
from django.utils.translation import gettext_lazy as _
from core.apps.catalogue.models import Product
from core.apps.account.models import Address
from django.conf import settings
from django.db import models
import uuid

class Order(models.Model):
  class Status(models.TextChoices):
    PENDING = 'PENDING', ('Pending')
    APPROVED = 'APPROVED', ('Approved')
    FAILURE = 'FAILURE', ('Failure')

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_customers')
  address = models.ForeignKey(Address, on_delete=models.PROTECT)
  payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='payment method')
  status = models.CharField(max_length=30, choices=Status.choices, default=Status.PENDING)
  installments = models.SmallIntegerField(blank=True, null=True, verbose_name='number of installments')
  bank_slip_url = models.URLField(blank=True, null=True, verbose_name='billet url')
  remote_id = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Remote invoice ID',
  help_text='Remote invoice id at the payment gateway')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
  
  class Meta:
    verbose_name = _('order')

  @property
  def total(self):
    sum = 0
    for item in self.order_items.all():
      sum += item.price * item.quantity
    return sum

class OrderItem(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item_product')
  quantity = models.PositiveIntegerField(default=1)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

  class Meta:
    verbose_name = _('order item')
    ordering = ('-created_at',)

  def __str__(self):
    return str(self.created_at)