from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ['place']
    list_display = ['id', 'place']
    ordering = ('id', 'place',)
