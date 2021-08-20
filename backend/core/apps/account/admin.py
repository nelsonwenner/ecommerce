from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from core.apps.my_admin.admin import admin_site
from core.apps.account.models import Customer

class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('username', 'email', 'password',)}),
    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}), 
    (('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )

  form = UserChangeForm
  add_form = UserCreationForm
  list_display = ('username', 'email', 'is_active', 'is_superuser', 'is_staff',)
  search_fields = ('email',)
  filter_horizontal = ('groups', 'user_permissions',)

admin_site.register(Customer, UserAdmin)
admin_site.register(Permission)
admin_site.register(Group)