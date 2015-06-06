from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin
from models import Bird, SharedBird


class BirdAdmin(DjangoMpttAdmin):
    pass


class SharedBirdAdmin(DjangoMpttAdmin):
    pass


admin.site.register(SharedBird, SharedBirdAdmin)
admin.site.register(Bird, BirdAdmin)
