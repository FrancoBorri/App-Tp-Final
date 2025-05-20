from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, QuestionViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r"", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"questions", QuestionViewSet, basename="question")
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = router.urls
