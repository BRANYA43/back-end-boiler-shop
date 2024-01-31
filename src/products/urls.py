from rest_framework.routers import DefaultRouter

from products import views

app_name = 'products'

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'specification', views.SpecificationViewSet)

urlpatterns = router.urls
