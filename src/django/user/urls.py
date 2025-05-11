from django.urls import path
from .views import RegisterView
from .views import UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # User register
    path(
        "login/", TokenObtainPairView.as_view(), name="login"
    ),  # Create acces_token and refresh_token
    path("profile/", UserProfileView.as_view(), name="user_profile"),  # User profile
]
