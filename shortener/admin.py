from django.contrib import admin
from .models import Url
from django.contrib.auth.models import Group
from django.contrib import admin


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    ordering = ['-create']
    list_display = ['ip', 'uuid', 'create']
    readonly_fields = ['ip', 'url', 'uuid', 'create']
    list_filter = ['create', ]
    search_fields = ['url', ]
    list_per_page = 50

    search_help_text = 'Search in urls'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
