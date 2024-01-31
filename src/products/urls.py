from rest_framework.routers import DefaultRouter

from products import views


router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'specification', views.SpecificationViewSet)
router.register(r'product-image-set', views.ProductImageSetViewSet, basename='product-image-set')

urlpatterns = router.urls
