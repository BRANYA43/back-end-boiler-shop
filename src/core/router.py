from rest_framework.routers import DefaultRouter
from orders import views as orders_views

router = DefaultRouter()

router.register(r'order', orders_views.OrderViewSet)
router.register(r'customer', orders_views.CustomerViewSet)
router.register(r'order-product', orders_views.OrderProductViewSet)
