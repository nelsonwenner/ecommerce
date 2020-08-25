from common.models import BaseCustomer, AutoCreateUpdatedMixin
from payment_gateway.models import PaymentMethod
from auth_core.models import UserClient
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
import uuid
import os

class Customer(BaseCustomer):
    user = models.OneToOneField(UserClient, on_delete=models.CASCADE, related_name='user_client')
    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'client'

    def __str__(self):
        return self.user.email

class Address(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='user_client_address')
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'address'

    def __str__(self):
        return self.city

class Status(AutoCreateUpdatedMixin):

    STATUS = (
        ('Processing Purchase', 'Processing Purchase'),
        ('Approved Purchase', 'Approved Purchase'),
        ('Purchase Denied', 'Purchase Denied'),
        ('Purchase Denied', 'Purchase sent'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(max_length=30, choices=STATUS)
    
    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'

    def __str__(self):
        return self.message

class Category(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='name')
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
def hash_filename_to_uuid(instance, filename):
    ext = os.path.splitext(filename)
    new_filename = "{0}{1}".format(uuid.uuid4(), ext)
    return new_filename

def upload_to(instance, filename):
    new_filename = hash_filename_to_uuid(instance, filename)
    return os.path.join(settings.MEDIA_BASE_PATH + '/product/', new_filename)

class Product(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_product")
    image = models.ImageField(max_length=255, upload_to=upload_to)
    
    class Meta:
        verbose_name = 'product'

    def __str__(self):
        return self.title

class Checkout(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='user_client_checkout')
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='payment method')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, related_name="status")
    installments = models.SmallIntegerField(blank=True, null=True, verbose_name='number of installments')
    bank_slip_url = models.URLField(blank=True, null=True, verbose_name='billet url')
    remote_id = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Remote invoice ID',
    help_text='Remote invoice id at the payment gateway')
    
    class Meta:
        verbose_name = 'checkout'
        
    @property
    def total(self):
        sum = 0
        for item in self.checkout_items.all():
            sum += item.price * item.quantity
        return sum

class CheckoutItem(AutoCreateUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name="checkout_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="checkout_item_product")
    quantity = models.PositiveSmallIntegerField(verbose_name='quantity')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='price')

    class Meta:
        verbose_name = 'checkout item'

    def __str__(self):
        return "Email: {} Date: {}".format(self.checkout.customer.email, self.created_at)