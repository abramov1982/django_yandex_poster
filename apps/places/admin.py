from django.contrib import admin

from .models import *
# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ['place']
    list_display = ['number', 'place']
    ordering = ('number', 'place',)


@admin.register(PlaceCoord)
class PlaceCoordAdmin(admin.ModelAdmin):
    list_display = ['title', 'placeId']

