from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.auth.forms import AuthenticationForm

class AdminSite(DjangoAdminSite):
    site_header = "Admin Owner"
    site_title = "Admin Owner"
    index_title = "Welcome Admin Owner"
    login_form = AuthenticationForm

admin_site = AdminSite(name="admin_site")