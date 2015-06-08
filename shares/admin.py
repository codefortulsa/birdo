from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Share, SearchTag, BirdSearchResult
from birds.models import Bird


# class ShareBirdInlineAdmin(admin.TabularInline):
#     model = Bird


class ShareAdmin(OSMGeoAdmin):
    # inlines = (ShareBirdInlineAdmin,)
    fields = ('user', 'network', 'rel', 'posted', 'location', 'tags', 'text')
    list_display = ('network', 'user', 'posted', 'rel', 'display_birds', 'location')
    list_filter = ('birds',)
    default_zoom = 2

    def display_birds(self, object):
        return ', '.join(map(lambda bird: str(bird), object.birds.all()))


class SearchTagAdmin(admin.ModelAdmin):
    pass


class BirdSearchResultAdmin(admin.ModelAdmin):
    list_display = ('target_bird', 'last_network_id', 'count', 'created',)


admin.site.register(Share, ShareAdmin)
admin.site.register(SearchTag, SearchTagAdmin)
admin.site.register(BirdSearchResult, BirdSearchResultAdmin)
