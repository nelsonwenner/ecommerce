from django.contrib.admin import ModelAdmin
from my_admin.admin import admin_site
from django.contrib import admin
from core.models import *

@admin.register(Category, site=admin_site)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Book, site=admin_site)
class BookAdmin(ModelAdmin):
    search_fields = ('title',)

@admin.register(CreditCard, site=admin_site)
class CreditCardAdmin(ModelAdmin):
    search_fields = ('number',)

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
    list_display = ('get_customer', 'status', 'get_total')
    inlines = (CheckoutInline, )

    def get_customer(self, obj):
        return obj.customer.email

    get_customer.short_description = 'client'

    def get_total(self, obj):
        return obj.total

    get_total.short_description = 'total'

@admin.register(Author, site=admin_site)
class AuthorAdmin(ModelAdmin):
    pass

@admin.register(Write, site=admin_site)
class WriteAdmin(ModelAdmin):
    pass

@admin.register(Customer, site=admin_site)
class CustomerAdmin(ModelAdmin):
    exclude = ['user']
    list_display = ('name', 'email')

@admin.register(Address, site=admin_site)
class AddressAdmin(ModelAdmin):
    pass
