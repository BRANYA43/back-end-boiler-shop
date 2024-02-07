from rest_framework.routers import DefaultRouter
from products import views as products_views
from orders import views as orders_views

router = DefaultRouter()

router.register(r'category', products_views.CategoryViewSet)
router.register(r'product', products_views.ProductViewSet)
router.register(r'specification', products_views.SpecificationViewSet)
router.register(r'product-image-set', products_views.ProductImageSetViewSet)

router.register(r'order', orders_views.OrderViewSet)
router.register(r'customer', orders_views.CustomerViewSet)
router.register(r'order-product', orders_views.OrderProductViewSet)
