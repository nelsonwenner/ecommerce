from django.contrib.admin import ModelAdmin
from my_admin.admin import admin_site
from django.contrib import admin
from core.models import Book

@admin.register(Book, site=admin_site)
class BookAdmin(ModelAdmin):
    search_fields = ('title',)
