from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [

    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)