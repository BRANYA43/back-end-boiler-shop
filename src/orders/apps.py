from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from orders.signals import create_customer  # noqa
        from orders.signals import set_order_product_price  # noqa
