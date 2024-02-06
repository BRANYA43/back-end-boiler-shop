import admin_thumbnails
from django.contrib import admin

from utils.models import Attribute, Image


@admin.register(Image)
@admin_thumbnails.thumbnail('image')
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumbnail', 'updated', 'created')
    fields = ('name', 'image', 'updated', 'created')
    readonly_fields = ('updated', 'created')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    fields = ('name', 'value')
    search_fields = ('name', 'value')
    ordering = ('name',)
