from django.contrib import admin
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import *
# Register your models here.


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height='200px')
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    search_fields = ['place_coord__title']


@admin.register(PlaceCoord)
class PlaceCoordAdmin(admin.ModelAdmin):
    list_display = ['title', 'placeId']
    exclude = ('detailsUrl',)
