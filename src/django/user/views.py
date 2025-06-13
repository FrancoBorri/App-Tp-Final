
# Create your views here.
from django.contrib.auth import authenticate, login
from rest_framework import status
from .models import User_profile
from .serializers import RegisterSerializer
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserProfileView(viewsets.ModelViewSet):
    """
    ViewSet for user profile.
    """

    serializer_class = UserProfileSerializer
    queryset = User_profile.objects.all()
    permission_classes = [IsAuthenticated]

    # Crea un perfil a travez del usuario atenticado
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(APIView):
    """
    API view for user registration.
    """

    def post(self, request):
        """
        Handle user registration.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "user": serializer.data,
                    "message": "User registered successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "errors": serializer.errors,
                "message": "User registration failed.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


