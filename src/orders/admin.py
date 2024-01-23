from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'status', 'delivery', 'payment', 'is_paid', 'updated', 'created']
    fields = ['uuid', 'status', 'payment', 'is_paid', 'delivery', 'delivery_address', 'updated', 'created']
    readonly_fields = ['uuid', 'updated', 'created']
    ordering = ['created']
    list_filter = ['status', 'delivery', 'payment', 'is_paid']
    search_fields = ['comment', 'delivery_address']
