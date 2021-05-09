from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from my_admin.admin import admin_site
from auth_core.models import User

class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','email')}),
        (('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
        'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin_site.register(User, UserAdmin)