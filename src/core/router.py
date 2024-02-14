from rest_framework.routers import DefaultRouter
from products import views as product_views

router = DefaultRouter()

router.register(r'category', product_views.CategoryViewSet)
router.register(r'product', product_views.ProductViewSet)
