from rest_framework.routers import DefaultRouter

from products import views

app_name = 'products'

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)

urlpatterns = router.urls
