from django.contrib import admin

from orders.models import Order, Customer, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    fields = ['product', 'quantity', 'price']
    extra = 0


class CustomerInline(admin.StackedInline):
    model = Customer
    fields = ['full_name', 'email', 'phone']


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    fields = ['order', 'product', 'quantity', 'price', 'total_cost']
    readonly_fields = ['total_cost']

    def total_cost(self, instance):
        return str(instance.total_cost)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['order', 'full_name', 'email', 'phone']
    fields = ['order', 'full_name', 'email', 'phone']
    search_fields = ['full_name', 'email', 'phone']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'status', 'delivery', 'payment', 'is_paid', 'total_cost', 'updated', 'created']
    fields = [
        'uuid',
        'status',
        'payment',
        'is_paid',
        'delivery',
        'delivery_address',
        'total_cost',
        'updated',
        'created',
    ]
    readonly_fields = ['uuid', 'total_cost', 'updated', 'created']
    ordering = ['created']
    list_filter = ['status', 'delivery', 'payment', 'is_paid']
    search_fields = ['comment', 'delivery_address']
    inlines = [CustomerInline, OrderProductInline]

    def total_cost(self, instance):
        return str(instance.total_cost)
