from django.contrib import admin

from orders.models import Order, Customer, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    fields = ('product', 'quantity', 'price')
    readonly_fields = ('price',)
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class CustomerInline(admin.StackedInline):
    model = Customer
    fields = ('full_name', 'email', 'phone')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('order', 'full_name', 'email', 'phone')
    fields = ('order', 'full_name', 'email', 'phone')
    search_fields = ('full_name', 'email', 'phone')

    def has_add_permission(self, request):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'status', 'is_paid', 'delivery', 'payment', 'total_cost', 'updated', 'created')
    fields = (
        'uuid',
        'status',
        'payment',
        'is_paid',
        'delivery',
        'delivery_address',
        'total_cost',
        'updated',
        'created',
    )
    readonly_fields = ('uuid', 'status', 'is_paid', 'total_cost', 'updated', 'created')
    ordering = ('-created',)
    list_filter = ('status', 'delivery', 'payment', 'is_paid')
    search_fields = (
        'comment',
        'delivery_address',
        'customer__full_name',
        'customer__email',
        'customer__phone',
        'products__name',
    )
    inlines = (CustomerInline, OrderProductInline)

    def total_cost(self, instance):
        return str(instance.total_cost)
