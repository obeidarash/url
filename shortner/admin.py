from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    ordering = ['-create']
    list_display = ['url', 'uuid', 'create']
