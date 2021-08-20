from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomAccountManager
from django.core.mail import send_mail
from django.utils import timezone
from django.db import models
import uuid

class Customer(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=30)
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)
  created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

  objects = CustomAccountManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    verbose_name = 'Accounts'
    verbose_name_plural = 'Accounts'

  @property
  def get_address(self):
    return self.user_address.all()

  def email_user(self, subject, message, from_email=None, **kwargs):
    send_mail(subject, message, from_email, [self.email], fail_silently=False, **kwargs)
  
  def __str__(self):
    return self.username

class Address(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customer = models.ForeignKey(Customer, verbose_name=_('Customer'), on_delete=models.CASCADE, related_name="user_address")
  city = models.CharField(_('City/State'), max_length=150)
  street = models.CharField(_('Street'), max_length=150)
  suite = models.CharField(_('Suite'), max_length=150)
  zipcode = models.CharField(_('Zipcode'), max_length=50)
  phone = models.CharField(_('Phone Number'), max_length=50)
  delivery_instructions = models.CharField(_('Delivery Instructions'), max_length=255)
  default = models.BooleanField(_('Default'), default=False)
  created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

  class Meta:
    verbose_name = 'Address'
    verbose_name_plural = 'Addresses'

  def __str__(self):
    return '{} Address'.format(self.customer.username)
