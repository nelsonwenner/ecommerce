from django.contrib.admin.apps import AdminConfig
from django.apps import AppConfig

class MyAdminConfig(AdminConfig):
  default_site = 'core.apps.my_admin.admin.EcommerceAdminArea'

class AdminConfig(AppConfig):
  name = 'my_admin'