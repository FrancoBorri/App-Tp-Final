from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from .views import UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r"profile", UserProfileView, basename="user_profile")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # User register
    path(
        "login/", TokenObtainPairView.as_view(), name="login"
    ),  # Create acces_token and refresh_token
]

urlpatterns += router.urls
