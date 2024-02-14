from rest_framework.routers import DefaultRouter
from products import views as product_views
from orders import views as order_views

router = DefaultRouter()

router.register(r'category', product_views.CategoryViewSet)
router.register(r'product', product_views.ProductViewSet)
router.register(r'order', order_views.OrderViewSet)
router.register(r'order-product', order_views.OrderProductViewSet)
