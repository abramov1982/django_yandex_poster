from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Image, Place


# Register your models here.


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html(mark_safe('<img src="{url}" height={height} />'.format(
                               url=obj.image.url,
                               height='200px')
                                    )
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    search_fields = ['title']
