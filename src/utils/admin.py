from django.contrib import admin

from utils.models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    fields = ['name', 'value']
    search_fields = ['name', 'value']
    ordering = ['name']
