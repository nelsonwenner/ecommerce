from .apps.my_admin.admin import admin_site
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
  path('admin/', admin_site.urls),
  path('accounts/', include('core.apps.account.urls')),
  path('catalogues/', include('core.apps.catalogue.urls')),
  path('orders/', include('core.apps.order.urls')),
  path('payments/', include('core.apps.payment_gateway.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)