from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = _('Orders')

    def ready(self):
        from orders.signals import create_customer  # noqa
        from orders.signals import set_order_product_price  # noqa
