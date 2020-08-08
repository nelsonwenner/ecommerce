from django.conf.urls.static import static
from django.urls import path, include
from my_admin.admin import admin_site
from django.conf import settings

urlpatterns = [

    path('admin/', admin_site.urls),
    path('', include('core.urls')),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)