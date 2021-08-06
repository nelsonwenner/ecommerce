from core.apps.payment_gateway.models import (PaymentMethod, PaymentMethodConfig, PagarmeGateway, PaymentGateway)
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from django.contrib.auth.forms import AuthenticationForm
from core.apps.catalogue.models import Category, Product
from core.apps.order.models import Order, OrderItem
from django.contrib.admin import AdminSite
from django.contrib import admin

class EcommerceAdminArea(AdminSite):
  site_header = 'Admin Owner'
  site_title = 'Admin Owner'
  index_title = 'Welcome Admin Owner'
  login_form = AuthenticationForm

admin_site = EcommerceAdminArea(name='EcommerceAdminArea')

@admin.register(Category, site=admin_site)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(Product, site=admin_site)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'regular_price', 'discount_price', 
  'in_stock', 'is_active', 'created_at', 'updated_at']
  list_editable = ['regular_price', 'discount_price', 'in_stock', 'is_active']
  list_filter = ['in_stock', 'is_active']
  exclude = ['users_wishlist']

@admin.register(OrderItem, site=admin_site)
class OrderItemAdmin(admin.ModelAdmin):
  list_display = ('get_customer', 'get_date')
  
  def get_customer(self, obj):
    return obj.order.customer.email

  get_customer.short_description = 'client'

  def get_date(self, obj):
    return obj.created_at

  get_date.short_description = 'date'

class OrderInline(admin.TabularInline):
  model = OrderItem

@admin.register(Order, site=admin_site)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('get_customer', 'payment_method', 'status', 'get_total')
  inlines = (OrderInline, )

  def get_customer(self, obj):
    return obj.customer.email

  get_customer.short_description = 'client'

  def get_total(self, obj):
    return obj.total

  get_total.short_description = 'total'

@admin.register(PaymentMethod, site=admin_site)
class PaymentMethodAdmin(admin.ModelAdmin):
  list_display = ('name', 'allow_installments')

@admin.register(PaymentMethodConfig, site=admin_site)
class PaymentMethodConfig(admin.ModelAdmin):
  pass

@admin.register(PagarmeGateway, site=admin_site)
class PagarmeGatewayAdmin(PolymorphicChildModelAdmin):
  base_model = PaymentGateway
  show_in_index = True

@admin.register(PaymentGateway, site=admin_site)
class PaymentGatewayAdmin(PolymorphicParentModelAdmin):
  base_model = PaymentGateway
  child_models = (PagarmeGateway,)