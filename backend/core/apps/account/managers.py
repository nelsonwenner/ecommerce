from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

class CustomAccountManager(BaseUserManager):
  def validateEmail(self, email):
    try:
      validate_email(email)
    except ValidationError:
      raise ValueError(_('You must provide a valid email address'))

  def _create_user(self, email, password, **extra_fields):
    if email:
      email = self.normalize_email(email)
      self.validateEmail(email)
    else:
      raise ValueError(_('Customer Account: You must provide an email address'))
  
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_user(self, email, password=None, **extra_fields):
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)

    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True')
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True')

    return self._create_user(email, password, **extra_fields)
