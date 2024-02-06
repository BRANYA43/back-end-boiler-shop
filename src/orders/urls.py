from orders import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', views.OrderViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'order-product', views.OrderProductViewSet)

urlpatterns = [] + router.urls
