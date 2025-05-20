from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "name": {"required": True},
            "price": {"required": True},
            "stock": {"required": True},
        }

        def validate_name(self, value):
            """
            Validate that the product name is not empty.
            """
            if not value.strip():
                raise serializers.ValidationError("Name cannot be empty.")
            return value

        def validate_price(self, value):
            """
            Validate that the product price is not empty.
            """
            if not value:
                raise serializers.ValidationError("Product price cannot be empty.")
            if value <= 0:
                raise serializers.ValidationError(
                    "Product stock price must be grater than 0"
                )
            return value

        def validate_stock(self, value):
            """
            Validate that the product stock is not empty.
            """
            if value is None:
                raise serializers.ValidationError("Product stock cannot be empty.")
            if value < 0:
                raise serializers.ValidationError("Product stock cannot be negative")
            return value

        def create(self, validated_data):
            """
            Create a new product with the provided validated data.
            """
            return Product.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update the product with the provided validated data.
            """
            for key, attr in validated_data.items():
                setattr(instance, key, attr)
            instance.save()
            return instance
