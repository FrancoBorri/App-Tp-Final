from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "name": {"required": True},
        }

        def validate_name(self, value):
            """
            Validate that the category name is not empty.
            """
            if not value:
                raise serializers.ValidationError("Category name cannot be empty.")
            return value

        def create(self, validated_data):
            """
            Create a new category with the provided validated data.
            """
            return Category.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update the category with the provided validated data.
            """
            instance.name = validated_data.get("name", instance.name)
            instance.save()
            return instance
