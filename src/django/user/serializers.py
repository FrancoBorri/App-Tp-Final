from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User_profile

User = get_user_model()  # User default model django


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile.
    """

    class Meta:
        model = User_profile
        fields = ("address", "phone", "picture_profile")
        extra_kwargs = {
            "address": {"required": True},
            "phone": {"required": False},
            "picture_profile": {"required": False},
        }

        def validate_address(self, value):
            """
            Validate that the address is not empty.
            """
            if not value:
                raise serializers.ValidationError("Address cannot be empty.")
            return value

        def create(self, validated_data):
            """
            Create a new user profile with the provided validated data.
            """
            return User_profile.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update the user profile with the provided validated data.
            """
            instance.address = validated_data.get("address", instance.address)
            instance.phone = validated_data.get("phone", instance.phone)
            instance.picture_profile = validated_data.get(
                "picture_profile", instance.picture_profile
            )
            instance.save()
            return instance


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, value):
        """
        Validate password using Django's built-in validators.
        """
        validate_password(value)
        return value

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
