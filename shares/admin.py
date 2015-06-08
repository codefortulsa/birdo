from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Share, SearchTag


class ShareAdmin(OSMGeoAdmin):
    fields = ('user', 'network', 'rel', 'posted', 'location', 'tags', 'text')
    list_display = ('network', 'user', 'posted', 'rel', 'location')
    default_zoom = 2


class SearchTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Share, ShareAdmin)
admin.site.register(SearchTag, SearchTagAdmin)
