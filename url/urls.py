from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('shortner.urls')),
]

admin.site.site_header = "URL Shortner"
admin.site.site_title = "URL Shortner"
admin.site.index_title = "Welcome to URL Shortner Admin Area"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
