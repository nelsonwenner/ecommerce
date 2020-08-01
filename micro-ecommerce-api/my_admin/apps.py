from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    name = 'my_admin'
    default_site = 'admin.admin.AdminSite'