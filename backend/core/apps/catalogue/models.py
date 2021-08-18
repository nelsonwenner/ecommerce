from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from django.urls import reverse
from django.db import models
import uuid
import os

class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(verbose_name=_('Category Name'), 
  help_text=_('Required and unique'), max_length=255, unique=True, db_index=True)
  slug = AutoSlugField(populate_from='name')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
  updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

  class Meta:
    verbose_name = _('Category')
    verbose_name_plural = _('Categories')

  def get_absolute_url(self):
    return reverse("catalogue:category-list", args=[self.slug])

  def __str__(self):
    return self.name

def hash_filename_to_uuid(instance, filename):
  ext = os.path.splitext(filename)
  new_filename = "{0}{1}".format(uuid.uuid4(), ext)
  return new_filename

def upload_to(instance, filename):
  new_filename = hash_filename_to_uuid(instance, filename)
  return os.path.join(settings.MEDIA_BASE_PATH + '/product/', new_filename)

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="user_products")
  title = models.CharField(verbose_name=_("title"),help_text=_("Required"),max_length=255)
  description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
  image = models.ImageField(max_length=255, upload_to=upload_to)
  slug = AutoSlugField(populate_from='title')
  in_stock = models.BooleanField(verbose_name=_("Product in stock"),default=True)
  regular_price = models.DecimalField(verbose_name=_("Regular price"),
  help_text=_("Maximum 999.99"), error_messages={"name": {"max_length": 
  _("The price must be between 0 and 999.99."),},},max_digits=5,decimal_places=2)
  discount_price = models.DecimalField(verbose_name=_("Discount price"),
  help_text=_("Maximum 999.99"),error_messages={"name": {"max_length": 
  _("The price must be between 0 and 999.99."),},},max_digits=5,decimal_places=2)
  is_active = models.BooleanField(verbose_name=_("Product visibility"),
  help_text=_("Change product visibility"),default=True)
  users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)
  created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

  class Meta:
    ordering = ('-created_at',)
    verbose_name = _('Product')
    verbose_name_plural = _('Products')

  def __str__(self):
    return self.title