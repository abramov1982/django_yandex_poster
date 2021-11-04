from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height='200px')
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ['place']
    list_display = ['number', 'place']
    ordering = ('number', 'place',)
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


@admin.register(PlaceCoord)
class PlaceCoordAdmin(admin.ModelAdmin):
    list_display = ['title', 'placeId']

