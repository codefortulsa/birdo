from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Bird, PermutationType, BirdPermutation


class BirdPermutationInlineAdmin(admin.TabularInline):
    model = BirdPermutation
    extra = 1


class BirdAdmin(DjangoMpttAdmin):
    inlines = (BirdPermutationInlineAdmin,)
    fields = ('name', 'parent', 'vispedia_id',)


class PermutationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bird, BirdAdmin)
admin.site.register(PermutationType, PermutationTypeAdmin)
