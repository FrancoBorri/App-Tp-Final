from django.shortcuts import render

# Create your views here.
from rest_framework import status
from .serializers import RegisterSerializer
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    """
    API view for user profile.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handle GET request to retrieve user profile.
        """
        user = request.user.profile
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to create user profile.
        """
        try:
            if hasattr(
                request.user.profile, "profile"
            ):  # request.user is the user object authenticated
                return Response({"message": "Profile already exists."}, status=400)
        except:
            pass
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "user": serializer.data,
                    "message": "User profile created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "errors": serializer.errors,
                "message": "User profile creation failed.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request):
        """
        Handle PUT request to update user profile.
        """
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {
                "errors": serializer.errors,
                "message": "User profile update failed.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request):
        """
        Handle DELETE request to delete user profile.
        """
        user = request.user.profile
        if not user:
            return Response(
                {
                    "message": "User profile does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        user.delete()
        return Response(
            {
                "message": "User profile deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )


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
