from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import ModelAdmin
from payment_gateway.models import *
from django.contrib import admin
from core.models import *

class AdminSite(DjangoAdminSite):
    site_header = "Admin Owner"
    site_title = "Admin Owner"
    index_title = "Welcome Admin Owner"
    login_form = AuthenticationForm

admin_site = AdminSite(name="admin_site")

@admin.register(Category, site=admin_site)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Product, site=admin_site)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'price', 'stock')
    search_fields = ('title',)

@admin.register(Status, site=admin_site)
class StatusAdmin(ModelAdmin):
    pass

@admin.register(CheckoutItem, site=admin_site)
class CheckoutItemAdmin(ModelAdmin):
    list_display = ('get_customer', 'get_date')
    
    def get_customer(self, obj):
        return obj.checkout.customer.email

    get_customer.short_description = 'client'

    def get_date(self, obj):
        return obj.created_at

    get_date.short_description = 'date'

class CheckoutInline(admin.TabularInline):
    model = CheckoutItem

@admin.register(Checkout, site=admin_site)
class CheckoutAdmin(ModelAdmin):
    list_display = ('get_customer', 'payment_method', 'status', 'get_total')
    inlines = (CheckoutInline, )

    def get_customer(self, obj):
        return obj.customer.email

    get_customer.short_description = 'client'

    def get_total(self, obj):
        return obj.total

    get_total.short_description = 'total'

@admin.register(Customer, site=admin_site)
class CustomerAdmin(ModelAdmin):
    exclude = ['user']
    list_display = ('name', 'email')

@admin.register(Address, site=admin_site)
class AddressAdmin(ModelAdmin):
    pass

@admin.register(PaymentMethod, site=admin_site)
class PaymentMethodAdmin(ModelAdmin):
    list_display = ('name', 'allow_installments')

@admin.register(PaymentMethodConfig, site=admin_site)
class PaymentMethodConfig(ModelAdmin):
    pass

@admin.register(PagarmeGateway, site=admin_site)
class PagarmeGatewayAdmin(PolymorphicChildModelAdmin):
    base_model = PaymentGateway
    show_in_index = True

@admin.register(PaymentGateway, site=admin_site)
class PaymentGatewayAdmin(PolymorphicParentModelAdmin):
    base_model = PaymentGateway
    child_models = (PagarmeGateway,)

