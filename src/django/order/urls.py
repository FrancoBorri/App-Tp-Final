from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderProductViewSet


router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"order_product", OrderProductViewSet, basename="order_product")

urlpatterns = router.urls
